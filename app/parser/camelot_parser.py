import camelot.io as camelot
import pandas as pd


def extract_tables_camelot(pdf_path):

    extracted_tables = []

    try:

        tables = camelot.read_pdf(pdf_path,pages="all",flavor="lattice")

        for idx, table in enumerate(tables):
            df = table.df

            # ✅ remove empty rows
            df = df.dropna(axis=0,how="all")

            # ✅ remove empty cols
            df = df.dropna(axis=1,how="all")

            extracted_tables.append({"table_id":f"camelot_table_{idx}","page":table.page,"df": df})

            print(f"✅ Camelot table extracted: {idx}")

    except Exception as e:
        print(f"❌ Camelot extraction failed: {e}")

    return extracted_tables