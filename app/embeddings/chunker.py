def dataframe_to_chunks(table):

    chunks = []

    df = table["df"]

    page = table["page"]

    table_id = table["table_id"]

    for idx, row in df.iterrows():

        values = [
            str(v)
            for v in row.values
        ]

        text = " | ".join(values)

        chunks.append({
            "id": f"{table_id}_row_{idx}",
            "text": text,

            "metadata": {
                "page": page,
                "table_id": table_id,

                # ✅ searchable metadata
                "row_index": idx,
                "source": "table"
            }
        })

    return chunks