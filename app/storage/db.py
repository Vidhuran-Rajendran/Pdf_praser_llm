import duckdb

conn = duckdb.connect("data.db")

# create table
conn.execute("""
CREATE TABLE IF NOT EXISTS metrics (
    entity TEXT,
    attribute TEXT,
    value TEXT,
    unit TEXT,
    dimension TEXT
)
""")

def insert_records(records):
    for r in records:
        conn.execute("""
        INSERT INTO metrics VALUES (?, ?, ?, ?, ?)
        """, (
            r.get("entity"),
            r.get("attribute"),
            r.get("value"),
            r.get("unit"),
            r.get("dimension")
        ))


def fetch_all():
    return conn.execute("SELECT * FROM metrics").fetchall()
