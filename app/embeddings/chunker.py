def dataframe_to_chunks(table):

    df = table["df"]

    page = table["page"]

    table_id = table["table_id"]

    rows = []

    for _, row in df.iterrows():

        values = [

            str(v).strip()

            for v in row.values
        ]

        row_text = " | ".join(values)

        rows.append(row_text)

    # ✅ FULL TABLE CHUNK
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