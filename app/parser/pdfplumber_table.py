import pdfplumber
import pandas as pd


def extract_tables_pdf(pdf_path):

    tables = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            raw_tables = page.extract_tables()

            if not raw_tables:
                continue

            for table_id, table in enumerate(raw_tables):
                df = pd.DataFrame(table)

                # ✅ remove fully empty rows
                df = df.dropna(axis=0, how="all")

                # ✅ remove fully empty cols
                df = df.dropna(axis=1, how="all")

                # ✅ preserve all structure
                df = df.fillna(None)

                tables.append({
                    "page": page_num,
                    "table_id": f"page_{page_num}_table_{table_id}",
                    "df": df
                })

                print(f"✅ Table extracted from page {page_num}")

    return tables