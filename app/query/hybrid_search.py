from app.query.semantic_search import semantic_search
from app.query.keyword_search import keyword_search
from app.reranker.reranker import rerank_results

def hybrid_search(query):

    semantic = semantic_search(
        query,
        top_k=10
    )
    semantic = dict(semantic)

    semantic_docs = []

    docs = semantic["documents"][0]
    metas = semantic["metadatas"][0]

    for doc, meta in zip(docs, metas):

        semantic_docs.append({
            "document": doc,
            "metadata": meta,
            "source": "semantic"
        })

    keyword_docs = keyword_search(query)

    combined = semantic_docs + keyword_docs

    # ✅ deduplicate
    unique = {}

    for item in combined:
        unique[item["document"]] = item

    final_docs = list(unique.values())

    # ✅ rerank
    reranked = rerank_results(
        query,
        final_docs
    )

    return reranked[:5]