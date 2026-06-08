import re

# app/embeddings/chunker.py - replace entire file

def dataframe_to_chunks(table):
   df = table["df"]
   page = table["page"]
   table_id = table["table_id"]

   rows = []
   for _, row in df.iterrows():
       values = [str(v).strip() for v in row.values]
       cleaned = [v for v in values if v.lower()not in ["nan","none",""]]
       row_text = " | ".join(cleaned)
       rows.append(row_text)

   full_text = "\n".join(rows)

   return [{
       "id": table_id,
       "text": full_text,
       "metadata": {
           "page": page,
           "table_id": table_id,
           "source": "table"
       }
   }]
   
   
def is_section_header(row_text):

    row = row_text.strip()

    if not row:
        return False

    # ✅ mostly text
    has_number = bool(re.search(r"\d", row))
    # ✅ short/title-like
    short_line = len(row.split()) <= 6
    # ✅ many uppercase chars
    upper_ratio = (sum(c.isupper() for c in row)/ max(len(row), 1))

    # ✅ semantic section header
    if (
        not has_number and
        (
            upper_ratio > 0.3 or
            short_line
        )
    ):

        return True

    return False
