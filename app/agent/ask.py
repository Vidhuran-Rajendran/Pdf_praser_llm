import ollama
import re
from app.agent.graph import run_agent
from app.memory.session_memory import add_message
from app.context.query_rewritter import rewrite_query
from app.context.context_deduplicator import deduplicate_context
from app.context.context_builder import build_structured_context
from app.context.reasoning_prompt import build_reasoning_prompt

from app.embeddings.embedder import create_embedding
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def ask_question(query):

    # ✅ save user query
    add_message("user",query)
    
    enhanced_query = rewrite_query(query)
    tool_output = run_agent(enhanced_query)
    results = tool_output["results"]
    # ✅ APPLY DVP FILTER HERE
    filtered_results = filter_by_dvp(query, results)
    cleaned_chunks = deduplicate_context(filtered_results)
    context = build_structured_context(cleaned_chunks)
    prompt = build_reasoning_prompt(query,context)
    
    response = ollama.chat(model="qwen2.5",messages=[{"role": "user","content": prompt}])
    answer = response["message"]["content"]
    print("tool: ", tool_output["tool"])
    #print("result : ", tool_output["results"][:2])

    # ✅ store assistant response
    add_message("assistant",answer)
    return answer

def filter_by_dvp(query, results):
    query_emb = np.array(create_embedding(query)).reshape(1, -1)
    scored = []
    for r in results:
        dvp_text = r["metadata"].get("dvp_text")
        if not dvp_text:
            continue
        dvp_emb = np.array(create_embedding(dvp_text)).reshape(1, -1)
        score = cosine_similarity(query_emb,dvp_emb)[0][0]
        if score<0.5:
            continue
        scored.append((score, r))

    scored.sort(reverse=True, key=lambda x: x[0])

    return [r for s, r in scored[:5]]




def detect_project(query):
    match = re.search(r"\b[A-Z]{1,4}\d{2,4}\b",query.upper())

    if match:
        return match.group(0)

    return None