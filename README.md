# Finance-RAG-Chatbot

# 💰 Finance & Investment RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot for answering finance and investment-related questions using PDF documents.

---

# Features

- PDF-based knowledge system
- FAISS Vector Database
- Semantic Search
- Finance-specific AI assistant
- Groq LLM integration
- Fast Retrieval-Augmented Responses

---

# Technologies Used

- Python
- LangChain
- FAISS
- Sentence Transformers
- Groq API
- RAG Architecture

---

# Project Workflow

1. Load PDF documents
2. Split into chunks
3. Create embeddings
4. Store embeddings in FAISS
5. Retrieve relevant chunks
6. Generate contextual answer

---

# Folder Structure

```bash
finance-investment-rag/
│
├── data/
├── store/
├── src/
│   ├── ingest.py
│   ├── retriever.py
│   ├── rag_chain.py
│   └── main.py
│
├── .env
├── requirements.txt
└── README.md
```

---

# Installation

## Step 1: Clone Repository

```bash
git clone <your_repo_link>
```

---

## Step 2: Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Add PDF Documents

Put all finance PDFs inside:

```bash
data/
```

Examples:
- Mutual Fund Guide
- Stock Market Basics
- Investment Planning
- RBI Reports

---

# Add API Key

Create `.env` file:

```env
GROQ_API_KEY=your_key_here
MODEL_NAME=llama3-70b-8192
```

---

# Create Vector Database

Run:

```bash
python src/ingest.py
```

This will:
- Read PDFs
- Create chunks
- Generate embeddings
- Store vectors in FAISS

---

# Run Chatbot

```bash
python src/main.py
```

---

# Example Questions

- What is SIP?
- Difference between equity and debt funds?
- What is portfolio diversification?
- Explain risk management in investment.
- What are blue-chip stocks?

---

# Future Improvements

- Streamlit UI
- Chat History
- Hybrid Search
- Reranking
- Multi-PDF Search
- Voice Assistant

---

