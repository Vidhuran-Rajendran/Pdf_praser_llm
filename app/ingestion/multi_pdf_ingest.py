import os
from app.ingestion.pipeline import process_pdf


def ingest_folder(folder_path):
    for file in os.listdir(folder_path):
        if file.lower().endswith(".pdf"):
            file_path = os.path.join(folder_path, file)
            print(f"\n✅ Ingesting: {file}")
            process_pdf(file_path)