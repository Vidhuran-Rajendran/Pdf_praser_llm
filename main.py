import os
import shutil
from app.ingestion.pipeline import process_pdf
from app.agent.ask import ask_question
from app.memory.session_memory import clear_history
from app.ingestion.multi_pdf_ingest import ingest_folder


PDF_FOLDER = r"E:\New folder\Pdf_praser_llm\data"

# # ✅ ingest only once
# if not os.path.exists("chroma_db"):
#     print("\n✅ Multi-PDF ingestion started...\n")
#     ingest_folder(PDF_FOLDER)
#     print("\n✅ Ingestion completed.\n")

# else:
#     print("\n✅ Existing DB found. Skipping ingestion.\n")


# while True:
#     query = input("\nAsk: ")

#     if query.lower() == "exit":
#         break

#     if query.lower() == "clear":
#         clear_history()
#         print("\n✅ Memory cleared.\n")
#         continue

#     response = ask_question(query)
#     print("\n=== RESPONSE ===\n")
#     print(response)

import os
from app.ingestion.multi_pdf_ingest import ingest_folder
from app.agent.ask import ask_question
from app.memory.session_memory import clear_history
from app.storage.duckdb_store import conn

PDF_FOLDER = r"E:\New folder\Pdf_praser_llm\data"

# ✅ check DuckDB row count, NOT chroma_db folder
def db_has_data():
   try:
       result = conn.execute(
           "SELECT COUNT(*) FROM engineering_chunks"
       ).fetchone()
       return bool(result and result[0])
   except:
       return False

if not db_has_data():
   print("\n✅ No data found. Starting ingestion...\n")
   ingest_folder(PDF_FOLDER)
   print("\n✅ Ingestion completed.\n")
else:
   print("\n✅ Data found. Skipping ingestion.\n")

while True:
   query = input("\nAsk: ")
   if query.lower() == "exit":
       break
   if query.lower() == "clear":
       clear_history()
       print("\n✅ Memory cleared.\n")
       continue
   response = ask_question(query)
   print("\n=== RESPONSE ===\n")
   print(response)