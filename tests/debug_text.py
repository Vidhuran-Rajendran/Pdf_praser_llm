# # run this standalone
# # from app.storage.duckdb_store import conn

# # rows = conn.execute("SELECT COUNT(*) FROM engineering_chunks").fetchall()
# # print("TOTAL ROWS:", rows)

# # sample = conn.execute("SELECT content FROM engineering_chunks LIMIT 3").fetchall()
# # for r in sample:
# #    print(r)
   
# from app.embeddings.vectordb import collection

# print("CHROMA COUNT:", collection.count())

# data = collection.get()
# print("SAMPLE DOC:", data["documents"][:2])
# from app.agent.router import route_query

# q = "what is the maximum temperature of front pad"
# print("ROUTE:", route_query(q))
# from app.agent.graph import run_agent

# out = run_agent("what is the maximum temperature of front pad")
# print("TOOL:", out["tool"])
# print("RESULTS:", out["results"][:3])

# tests/debug_chunks.py
from app.storage.duckdb_store import conn



rows = conn.execute("""
  SELECT chunk_id, page, table_id, content 
  FROM engineering_chunks
""").fetchall()

print(f"TOTAL CHUNKS: {len(rows)}\n")

for r in rows:
  print("---")
  print("ID:", r[0])
  print("PAGE:", r[1])
  print("TABLE:", r[2])
  print("CONTENT:", r[3])