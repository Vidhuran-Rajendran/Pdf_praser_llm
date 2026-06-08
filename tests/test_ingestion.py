from app.ingestion.pipeline import process_pdf
from app.storage.db import fetch_all
import os
import shutil


if os.path.exists("chroma_db"):
    shutil.rmtree("chroma_db")

if os.path.exists("engineering.db"):
    os.remove("engineering.db")
print("✅ Old DB removed")
result = process_pdf(r"D:\new_train\training\Pdf_praser_llm\data\0183-VP-TDM-06-08196-C006-1339-BRAKE THERMAL MAPPING CITY CONDITION Vehicle Dynamics.pdf")



print("\n✅ TOTAL CHUNKS:")
print(len(result["chunks"]))


