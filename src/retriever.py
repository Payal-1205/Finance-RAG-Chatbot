## =========================================================
## RETRIEVER
## =========================================================

from pathlib import Path
import pickle
import faiss

from sentence_transformers import SentenceTransformer


## =========================================================
## CONFIGURATION
## =========================================================

MODEL_NAME = "all-MiniLM-L6-v2"

BASE_DIR = Path(__file__).resolve().parent.parent

STORE_DIR = BASE_DIR / "store"

INDEX_PATH = STORE_DIR / "finance_faiss.index"
CHUNKS_PATH = STORE_DIR / "finance_chunks.pkl"


## Load embedding model
model = SentenceTransformer(MODEL_NAME)


## =========================================================
## RETRIEVAL FUNCTION
## =========================================================

def retriever(query, k=5):

    ## Check files exist
    if not INDEX_PATH.exists() or not CHUNKS_PATH.exists():

        raise FileNotFoundError(
            "Run ingest.py first to create vector database."
        )

    ## Load FAISS index
    index = faiss.read_index(str(INDEX_PATH))

    ## Load chunks
    with open(CHUNKS_PATH, "rb") as f:

        chunks = pickle.load(f)

    ## Convert query into embedding
    query_embedding = model.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True
    ).astype("float32")

    ## Search top-k
    distances, indices = index.search(query_embedding, k)

    results = []

    for i in indices[0]:

        results.append(chunks[i].page_content)

    return results