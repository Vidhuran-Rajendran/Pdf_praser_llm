from app.ingestion.pipeline import process_pdf
from app.storage.db import fetch_all

result = process_pdf(r"D:\new_train\training\Pdf_praser_llm\data\0183-VP-TDM-06-08196-C006-1339-BRAKE THERMAL MAPPING CITY CONDITION Vehicle Dynamics.pdf")


for t in result["tables"]:

    print("\n====================")
    print("TABLE:", t["table_id"])
    print("PAGE:", t["page"])

    print(t["df"])

