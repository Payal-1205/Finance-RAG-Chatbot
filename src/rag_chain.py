## =========================================================
## FINANCE RAG PIPELINE
## =========================================================

import os

from dotenv import load_dotenv
from groq import Groq

from retriever import retriever


## =========================================================
## LOAD ENV VARIABLES
## =========================================================

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "llama3-70b-8192"
)


## =========================================================
## GENERATE ANSWER
## =========================================================

def generate_answer(query):

    ## Retrieve context
    retrieved_chunks = retriever(query)

    context = "\n\n".join(retrieved_chunks)

    ## Finance System Prompt
    SYSTEM_PROMPT = """
You are a Finance & Investment AI Assistant.

Your task:
- Answer ONLY from the provided context.
- Explain financial concepts in simple language.
- If answer is not available, say:
  "I don't know based on the provided documents."

Topics include:
- Mutual Funds
- SIP
- Stock Market
- Investment Planning
- Risk Management
- Equity vs Debt
- Portfolio Diversification
- Financial Literacy
"""

    ## Final Prompt
    prompt = f"""
CONTEXT:
{context}

QUESTION:
{query}
"""

    ## LLM Response
    response = client.chat.completions.create(
        model=MODEL_NAME,

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },

            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3
    )

    return response.choices[0].message.content