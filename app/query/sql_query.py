from app.storage.duckdb_store import conn,initialize_db
initialize_db()
def run_sql(query):
    result = conn.execute(query).fetchall()
    return result