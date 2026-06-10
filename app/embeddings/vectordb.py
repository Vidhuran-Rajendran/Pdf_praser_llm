import chromadb
from app.embeddings.embedder import create_embedding

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="dvp_tables", embedding_function=None)

def store_chunks(chunks):
    ids = []
    docs = []
    metas = []
    embeddings = []

    for chunk in chunks:
        ids.append(chunk["id"])
        docs.append(chunk["text"])
        metas.append(chunk["metadata"])

        # ✅ YOUR BGE EMBEDDING
        emb = create_embedding(chunk["text"])
        embeddings.append(emb)

    # ✅ pass embeddings manually
    collection.add(ids=ids,
        documents=docs,
        metadatas=metas,
        embeddings=embeddings
    )
    
