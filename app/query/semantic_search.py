from app.embeddings.vectordb import (
    collection
)


def semantic_search(query, top_k=5):

    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )

    return results