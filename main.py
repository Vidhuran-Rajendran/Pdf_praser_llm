import os

from app.ingestion.pipeline import (
    process_pdf
)

from app.agent.ask import (
    ask_question
)

# ✅ your PDF path
PDF_PATH = r"D:\new_train\training\Pdf_praser_llm\data\0183-VP-TDM-06-08196-C006-1339-BRAKE THERMAL MAPPING CITY CONDITION Vehicle Dynamics.pdf"

# ✅ run ingestion only once
if not os.path.exists("chroma_db"):

    print("\n✅ First-time ingestion started...\n")

    process_pdf(PDF_PATH)

    print("\n✅ Ingestion completed.\n")

else:

    print("\n✅ Existing DB found. Skipping ingestion.\n")


# ✅ chat loop
while True:

    query = input("\nAsk: ")

    if query.lower() == "exit":
        break

    response = ask_question(query)

    print("\n=== RESPONSE ===\n")

    print(response)