from sentence_transformers import SentenceTransformer

model = SentenceTransformer(r"model\bge_model")


def create_embedding(text):

    return model.encode(text).tolist()