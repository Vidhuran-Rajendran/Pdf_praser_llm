# tests/force_ingest.py
import shutil
import os

# wipe stale empty DBs
if os.path.exists("chroma_db"):
   shutil.rmtree("chroma_db")

if os.path.exists("engineering.db"):
   os.remove("engineering.db")

print("Cleaned. Starting ingestion...")

from app.ingestion.pipeline import process_pdf

result = process_pdf(
   r"D:\new_train\training\Pdf_praser_llm\data\0183-VP-TDM-06-08196-C006-1339-BRAKE THERMAL MAPPING CITY CONDITION Vehicle Dynamics.pdf"
)

print("Pages:", len(result["pages"]))
print("Tables:", len(result["tables"]))
print("Chunks:", len(result["chunks"]))