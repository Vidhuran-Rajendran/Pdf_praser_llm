from app.embeddings.vectordb import collection


def keyword_search(keyword):

    data = collection.get()

    results = []

    docs = data["documents"] or []
    metas = data["metadatas"] or []

    for doc, meta in zip(docs, metas):

        if keyword.lower() in doc.lower():

            results.append({
                "document": doc,
                "metadata": meta
            })

    return results