def route_query(query):

    query = query.lower()

    sql_keywords = [

        "count",
        "total",
        "sum",
        "average",
        "compare",
        "page"

    ]

    for k in sql_keywords:

        if k in query:
            return "sql"

    return "rag"