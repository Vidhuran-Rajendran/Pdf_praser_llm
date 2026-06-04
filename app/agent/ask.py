import ollama
from app.query.hybrid_search import hybrid_search
from app.context.context_builder import build_context


def ask_question(query):

    results = hybrid_search(query)
    context = build_context(results)

    prompt = f"""
You are an automotive engineering assistant.

Use ONLY the provided context.

Context:
{context}

Question:
{query}
"""

    response = ollama.chat(
        model="qwen2.5",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]