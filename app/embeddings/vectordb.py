import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="dvp_tables"
)


def store_chunks(chunks):

    ids = []
    docs = []
    metas = []

    for chunk in chunks:

        ids.append(chunk["id"])

        docs.append(chunk["text"])

        metas.append(chunk["metadata"])

    collection.add(
        ids=ids,
        documents=docs,
        metadatas=metas
    )