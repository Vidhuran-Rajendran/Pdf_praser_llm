def route_query(query):

    query = query.lower()

    sql_keywords = [

        "count",
        "maximum",
        "minimum",
        "average",
        "compare",
        "page"

    ]

    for k in sql_keywords:

        if k in query:
            return "sql"

    return "rag"