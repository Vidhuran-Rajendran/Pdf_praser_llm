import ollama
from app.agent.graph import run_agent
from app.memory.session_memory import add_message
from app.context.conversation_context import build_conversation_context
from app.context.query_rewritter import rewrite_query

def ask_question(query):

    # ✅ save user query
    add_message("user",query)
    
    enhanced_query = rewrite_query(query)
    tool_output = run_agent(enhanced_query)
    retrieval_context = ""

    for r in tool_output["results"]:
        
        if isinstance(r, dict):
            retrieval_context += (str(r.get("document", ""))+ "\n")
            
        else:
            retrieval_context += (str(r)+ "\n")

    # ✅ previous conversation
    memory_context = (build_conversation_context())

    prompt = f"""

You are an automotive engineering assistant.

Answer ONLY from provided context.

If answer is unavailable, say:
"Answer not found in context."

====================
CONVERSATION MEMORY
====================
{memory_context}

====================
RETRIEVAL CONTEXT
====================
{retrieval_context}

====================
QUESTION
====================
{query}
"""

    response = ollama.chat(model="qwen2.5",messages=[{"role": "user","content": prompt}])
    answer = response["message"]["content"]

    # ✅ store assistant response
    add_message("assistant",answer)
    return answer