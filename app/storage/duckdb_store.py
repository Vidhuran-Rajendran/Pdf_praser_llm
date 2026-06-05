import duckdb

conn = duckdb.connect("engineering.db")

def initialize_db():

    conn.execute("""
    CREATE TABLE IF NOT EXISTS engineering_chunks (

        chunk_id TEXT,
        page INTEGER,
        table_id TEXT,
        row_index INTEGER,
        content TEXT
    )
    """)


def insert_chunks(chunks):

    for chunk in chunks:

        conn.execute("""

        INSERT INTO engineering_chunks
        VALUES (?, ?, ?, ?)

        """, (

            chunk["id"],

            chunk["metadata"]["page"],

            chunk["metadata"]["table_id"],
            
            chunk["metadata"]["row_index"],

            chunk["text"]

        ))
