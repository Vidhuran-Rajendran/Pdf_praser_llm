import ollama
from app.agent.graph import run_agent

def ask_question(query):
    tool_output = run_agent(query)
    context = ""
    # RAG context
    if tool_output["tool"] == "rag":

        for r in tool_output["results"]:
            context += (r["document"] + "\n")
    # SQL context
    else:
        for r in tool_output["results"]:
            context += (str(r) + "\n")
    prompt = f"""

You are an automotive engineering assistant.
Use ONLY the provided context.

Context:
{context}

Question:
{query}
"""
    response = ollama.chat(model="qwen2.5",messages=[{"role": "user","content": prompt}])
    return response["message"]["content"]