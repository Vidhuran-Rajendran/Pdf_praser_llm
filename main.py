import os
from app.ingestion.pipeline import process_pdf
from app.agent.ask import ask_question
from app.memory.session_memory import clear_history
from app.ingestion.multi_pdf_ingest import ingest_folder
import shutil

PDF_FOLDER = r"E:\New folder\Pdf_praser_llm\data"

# ✅ ingest only once

if os.path.exists("chroma_db"):
    shutil.rmtree("chroma_db")

if os.path.exists("engineering.db"):
    os.remove("engineering.db")

print("\n✅ Fresh ingestion started...\n")
ingest_folder(PDF_FOLDER)



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