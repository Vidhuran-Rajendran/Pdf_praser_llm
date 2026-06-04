from app.query.semantic_search import semantic_search
from app.query.keyword_search import keyword_search

def hybrid_search(query):

    semantic = semantic_search(
        query,
        top_k=5
    )

    keyword = keyword_search(
        query
    )

    return {
        "semantic_results": semantic,
        "keyword_results": keyword
    }