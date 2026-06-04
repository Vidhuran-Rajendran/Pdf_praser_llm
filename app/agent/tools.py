from app.query.hybrid_search import (
    hybrid_search
)

from app.query.structured_search import (
    structured_search
)


def rag_tool(query):

    results = hybrid_search(query)

    return {
        "tool": "rag",
        "results": results
    }


def sql_tool(query):

    results = structured_search(
        keyword=query
    )

    return {
        "tool": "sql",
        "results": results
    }