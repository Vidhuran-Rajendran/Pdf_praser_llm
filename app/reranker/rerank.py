from sentence_transformers import CrossEncoder

reranker = CrossEncoder(r"model\bge_reranker_model")


def rerank_results(query, documents):

    pairs = []

    for doc in documents:
        pairs.append([
            query,
            doc["document"]
        ])

    scores = reranker.predict(pairs)

    ranked = []

    for doc, score in zip(documents, scores):

        doc["rerank_score"] = float(score)

        ranked.append(doc)

    ranked = sorted(
        ranked,
        key=lambda x: x["rerank_score"],
        reverse=True
    )

    return ranked