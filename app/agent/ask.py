import ollama
from app.agent.graph import run_agent
from app.memory.session_memory import add_message
from app.context.conversation_context import build_conversation_context
from app.context.query_rewritter import rewrite_query
from app.context.conversation_context import build_conversation_context
from app.context.context_deduplicator import deduplicate_context
from app.context.context_builder import build_structured_context
from app.context.reasoning_prompt import build_reasoning_prompt

def ask_question(query):

    # ✅ save user query
    add_message("user",query)
    
    enhanced_query = rewrite_query(query)
    tool_output = run_agent(enhanced_query)
    cleaned_chunks = deduplicate_context(tool_output['results'])
    context = build_structured_context(cleaned_chunks)
    prompt = build_reasoning_prompt(query,context)
    
    response = ollama.chat(model="qwen2.5",messages=[{"role": "user","content": prompt}])
    answer = response["message"]["content"]
    print("tool: ", tool_output["tool"])
    print("result : ", tool_output["results"][:2])

    # ✅ store assistant response
    add_message("assistant",answer)
    return answer