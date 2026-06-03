from app.ingestion.pipeline import process_pdf

result = process_pdf(r"D:\new_train\training\Pdf_praser_llm\data\0183-VP-TDM-06-08196-C006-1339-BRAKE THERMAL MAPPING CITY CONDITION Vehicle Dynamics.pdf")
# print(result)
# for e in result["elements"][:10]:
#     print(e)

print("\n=== TITLES ===")
for t in result.get("titles", [])[:10]:
    print(t)

print("\n=== TEXT ===")
for t in result.get("text", [])[:10]:
    print(t)

print("\n=== TABLES ===")
for t in result.get("tables", [])[:5]:
    print(t)
