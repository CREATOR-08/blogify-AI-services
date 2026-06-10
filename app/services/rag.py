from app.services.retrieval import retrieve_context
from app.services.gemini import generate_response


def answer_question(question: str):

    context = retrieve_context(question)

    context_text = "\n\n".join(context)

    prompt = f"""
You are a current affairs assistant.

Answer ONLY using the provided context.

If information is missing, say:
"Information not found in retrieved documents."

CONTEXT:
{context_text}

QUESTION:
{question}
"""

    answer = generate_response(prompt)

    return {
        "question": question,
        "answer": answer,
        "sources": context
    }