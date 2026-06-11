def route_query(query):

    query = query.lower()

    sql_keywords = [

        "count",
        "how many",
        "page"

    ]

    for k in sql_keywords:

        if k in query:
            return "sql"

    return "rag"
def detect_dvp(query, available_dvps):

    query_lower = query.lower()

    for dvp in available_dvps:
        if any(word in dvp.lower() for word in query_lower.split()):
            return dvp

    return None