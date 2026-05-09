## =========================================================
## MAIN APPLICATION
## =========================================================

from rag_chain import generate_answer


def main():

    print("=" * 60)
    print("FINANCE & INVESTMENT RAG CHATBOT")
    print("=" * 60)

    print("\nAsk finance questions")
    print("Type 'exit' to quit.\n")

    while True:

        query = input("You: ")

        if query.lower() in ["exit", "quit"]:

            print("Goodbye!")
            break

        answer = generate_answer(query)

        print("\nAI:")
        print(answer)
        print()


if __name__ == "__main__":
    main()