# tests/test_camelot.py
from app.parser.camelot_parser import extract_tables_camelot

tables = extract_tables_camelot(
   r"D:\new_train\training\Pdf_praser_llm\data\0183-VP-TDM-06-08196-C006-1339-BRAKE THERMAL MAPPING CITY CONDITION Vehicle Dynamics.pdf"
)

print(f"TOTAL TABLES: {len(tables)}\n")

for t in tables:
   print("====================")
   print("TABLE ID:", t["table_id"])
   print("PAGE:", t["page"])
   print(t["df"].to_string())
   print()