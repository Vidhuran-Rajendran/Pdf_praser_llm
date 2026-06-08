from app.embeddings.vectordb import collection
from app.embeddings.embedder import create_embedding


def semantic_search(query, project=None,top_k=5):

    query_embedding = create_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        where ={"project": project}if project else None
    )

    return results
