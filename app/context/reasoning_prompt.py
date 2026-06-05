def build_reasoning_prompt(query, context):

    return f"""
You are an automotive engineering assistant.

Answer ONLY using the provided context.

If answer is not present, say:
"Answer not found in context."

Context:
{context}

Question:
{query}

Give concise factual answer.
"""