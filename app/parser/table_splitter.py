
def split_logical_tables(table):

    data = table["data"]

    split_tables = []
    current = []

    anchors = [
        "P201 BRAKE TEMPERATURE MAPPING",
        "Description",
        "PARAMETERS"
    ]

    for row in data:

        row_text = " ".join(row)

        # ✅ start new logical table
        if any(a in row_text for a in anchors):

            if current:
                split_tables.append(current)

            current = [row]

        else:
            current.append(row)

    if current:
        split_tables.append(current)

    final = []

    for idx, t in enumerate(split_tables):

        if len(t) >= 2:

            final.append({
                "table_id": f"{table['table_id']}_split_{idx}",
                "page": table["page"],
                "data": t
            })

    return final
