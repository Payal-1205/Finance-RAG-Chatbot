## =========================================================
## FINANCE & INVESTMENT RAG CHATBOT
## Ingest Pipeline
## =========================================================

from pathlib import Path
import pickle
import faiss
import numpy as np

## LangChain
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

## Embedding Model
from sentence_transformers import SentenceTransformer


## =========================================================
## CONFIGURATION
## =========================================================

EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
STORE_DIR = BASE_DIR / "store"

INDEX_PATH = STORE_DIR / "finance_faiss.index"
CHUNKS_PATH = STORE_DIR / "finance_chunks.pkl"


## =========================================================
## STEP 1 : LOAD PDF DOCUMENTS
## =========================================================

def load_documents(data_path):

    docs = []

    for file in data_path.glob("*.pdf"):

        print(f"Loading: {file.name}")

        loader = PyPDFLoader(str(file))

        docs.extend(loader.load())

    return docs


## =========================================================
## STEP 2 : SPLIT DOCUMENTS INTO CHUNKS
## =========================================================

def split_documents(docs):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(docs)

    return chunks


## =========================================================
## STEP 3 : CREATE EMBEDDINGS
## =========================================================

def create_embeddings(chunks):

    model = SentenceTransformer(EMBEDDING_MODEL_NAME)

    texts = [chunk.page_content for chunk in chunks]

    embeddings = model.encode(
        texts,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True
    ).astype("float32")

    return embeddings


## =========================================================
## STEP 4 : STORE EMBEDDINGS IN FAISS
## =========================================================

def store_faiss(embeddings, chunks):

    STORE_DIR.mkdir(exist_ok=True)

    dimension = embeddings.shape[1]

    ## cosine similarity
    index = faiss.IndexFlatIP(dimension)

    index.add(embeddings)

    ## save index
    faiss.write_index(index, str(INDEX_PATH))

    ## save chunks
    with open(CHUNKS_PATH, "wb") as f:
        pickle.dump(chunks, f)

    print("FAISS index stored successfully!")


## =========================================================
## MAIN
## =========================================================

if __name__ == "__main__":

    print("Loading finance documents...")

    docs = load_documents(DATA_DIR)

    print(f"Loaded {len(docs)} pages")

    print("Splitting documents...")

    chunks = split_documents(docs)

    print(f"Created {len(chunks)} chunks")

    print("Creating embeddings...")

    embeddings = create_embeddings(chunks)

    print(f"Embedding Shape: {embeddings.shape}")

    print("Saving to FAISS Vector DB...")

    store_faiss(embeddings, chunks)

    print("Finance RAG Knowledge Base Ready!")