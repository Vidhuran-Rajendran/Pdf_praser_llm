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

    tool_output = run_agent(query)
    is_compare = "compare" in query.lower()
    results = tool_output["results"]

    # ✅ STRICT DOCUMENT LOCK
    query_lower = query.lower()
    matched_docs = []

    for r in results:
        dvp = r["metadata"].get("dvp_text", "").lower()
        if any(word in dvp for word in query_lower.split()):
            matched_docs.append(r["metadata"]["doc_id"])

    if matched_docs:
        best_doc = matched_docs[0]   # ✅ PRIORITY
    else:
        # fallback normal logic
        doc_scores = {}
        for r in results:
            doc = r["metadata"].get("doc_id")
            if doc is None:
                continue
            doc_scores[doc] = doc_scores.get(doc, 0) + 1
        best_doc = max(doc_scores.items(), key=lambda item: item[1])[0]

    filtered_results = [r for r in results if r["metadata"].get("doc_id") == best_doc]
    
    if is_compare:
        filtered_results = results[:10]   # ✅ multi-doc
    else:
        filtered_results = [r for r in results if r["metadata"].get("doc_id") == best_doc]

    cleaned_chunks = deduplicate_context(filtered_results)
    context = build_structured_context(cleaned_chunks)
    prompt = build_reasoning_prompt(query, context)
    
    response = ollama.chat(
        model="qwen2.5",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response["message"]["content"]
    top_meta = filtered_results[0]["metadata"]

    return f"""
📄 PDF: {top_meta.get("pdf_name")}
📊 DVP: {top_meta.get("dvp_text")}
🖼 Image Path: {top_meta.get("image_path", "N/A")}

✅ Answer:
{answer}
"""




def filter_by_dvp(query, results):
    query_emb = np.array(create_embedding(query)).reshape(1, -1)
    scored = []
    for r in results:
        dvp_text = r["metadata"].get("dvp_text")
        if not dvp_text:
            continue
        dvp_emb = np.array(create_embedding(dvp_text)).reshape(1, -1)
        score = cosine_similarity(query_emb,dvp_emb)[0][0]
        # if score<0.5:
        #     continue
        scored.append((score, r))

    scored.sort(reverse=True, key=lambda x: x[0])

    return [r for s, r in scored[:5]]




def detect_project(query):
    match = re.search(r"\b[A-Z]{1,4}\d{2,4}\b",query.upper())

    if match:
        return match.group(0)

    return None