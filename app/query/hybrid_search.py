from app.query.semantic_search import semantic_search
from app.query.keyword_search import keyword_search
from app.reranker.rerank import rerank_results
from app.retrival.neighbor_retriever import get_neighbor_chunks

def hybrid_search(query):

    semantic = semantic_search(
        query,
        top_k=10
    )

    semantic_docs = []

    # semantic may be None or may not contain expected keys; guard safely
    if semantic and isinstance(semantic, dict):
        docs = semantic.get("documents")
        metas = semantic.get("metadatas")

        # documents/metadatas expected to be lists of lists; try to extract first inner list
        if docs and isinstance(docs, list):
            docs = docs[0] if len(docs) > 0 and isinstance(docs[0], list) else docs
        else:
            docs = []

        if metas and isinstance(metas, list):
            metas = metas[0] if len(metas) > 0 and isinstance(metas[0], list) else metas
        else:
            metas = []
    else:
        docs = []
        metas = []

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

    # ✅ MUST RETURN LIST
    expanded_results = []
    for r in reranked[:5]:
        expanded_results.append(r)
        metadata = r["metadata"]
        table_id = metadata["table_id"]
        row_index = metadata.get("row_index",0)
        neighbors = get_neighbor_chunks(table_id=table_id,row_index=row_index,window=2)

        for n in neighbors:
            expanded_results.append({"document": n,"metadata": metadata,"source": "neighbor"})

    return expanded_results