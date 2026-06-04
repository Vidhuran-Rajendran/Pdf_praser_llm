from app.query.sql_query import run_sql

def structured_search(keyword=None,
                      page=None,
                      table_id=None,
                      limit=20):
    conditions = []

    # ✅ keyword filter
    if keyword:

        conditions.append(f"LOWER(content) LIKE '%{keyword.lower()}%'")

    # ✅ page filter
    if page is not None:
        conditions.append(f"page = {page}")

    # ✅ table filter
    if table_id:
        conditions.append(f"table_id = '{table_id}'")
    query = """
    SELECT *
    FROM engineering_chunks
    """

    # ✅ dynamic WHERE
    if conditions:
        query += (" WHERE " +" AND ".join(conditions))
    query += f" LIMIT {limit}"

    return run_sql(query)
