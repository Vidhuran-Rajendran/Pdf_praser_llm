from app.storage.duckdb_store import conn

def get_neighbor_chunks(table_id, row_index, window=2):

    min_row = max(0, row_index - window)
    max_row = row_index + window

        
    query = f"""
    SELECT content
    FROM engineering_chunks
    WHERE table_id = '{table_id}'
    AND row_index BETWEEN {min_row} AND {max_row}
    """


    rows = conn.execute(query).fetchall()

    return [r[0] for r in rows]