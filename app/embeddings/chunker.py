import re

# app/embeddings/chunker.py - replace entire file


def dataframe_to_chunks(table, doc_id):

    df = table["df"]
    page = table["page"]
    table_id = table["table_id"]

    row_chunks = []
    rows = []

    for idx, row in df.iterrows():

        values = [str(v).strip() for v in row.values]
        cleaned = [v for v in values if v.lower() not in ["nan", "none", ""]]

        if not cleaned:
            continue

        row_text = " | ".join(cleaned)
        rows.append(row_text)

        # ✅ ROW CHUNK
        row_chunks.append({
            "id": f"{table_id}_{idx}",
            "text": row_text,
            "metadata": {
                "page": page,
                "table_id": table_id,
                "row_index": idx,
                "type": "row",
                "source": "table",
                "doc_id": doc_id
            }
        })

    # ✅ FULL TABLE CHUNK
    full_chunk = {
        "id": f"{table_id}_full",
        "text": "\n".join(rows),
        "metadata": {
            "page": page,
            "table_id": table_id,
            "type": "full_table",
            "source": "table",
            "doc_id": doc_id
        }
    }

    return row_chunks + [full_chunk]

   
   
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

def chunk_text_pages(pages):
   chunks = []
   for page_data in pages:
       page = page_data["page"]
       content = page_data.get("content", [])
       text_lines = [
           item["value"]
           for item in content
           if item["type"] == "text"
       ]
       buffer = []
       for line in text_lines:
           cleaned = line.strip()
           if not cleaned:
               continue
           buffer.append(cleaned)
           if len(buffer) >= 5:
               chunks.append({
                   "id": f"text_{page}_{len(chunks)}",
                   "text": "\n".join(buffer),
                   "metadata": {"page": page, "source": "text"}
               })
               buffer = []
       if buffer:
           chunks.append({
               "id": f"text_{page}_{len(chunks)}",
               "text": "\n".join(buffer),
               "metadata": {"page": page, "source": "text"}
           })
   return chunks