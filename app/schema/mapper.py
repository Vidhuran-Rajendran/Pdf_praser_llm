def map_table_to_schema(table):
    records = []

    columns = table["columns"]
    rows = table["rows"]

    # assume first column = metric
    for row in rows:
        if len(row) < 2:
            continue

        metric = row[0]

        for i in range(1, len(row)):
            value = row[i]

            if value.strip() == "":
                continue

            record = {
                "entity": "unknown",
                "attribute": metric,
                "value": value,
                "dimension": columns[i] if i < len(columns) else None
            }

            records.append(record)

    return records


def map_all_tables(tables):
    all_records = []

    for t in tables:
        recs = map_table_to_schema(t)
        all_records.extend(recs)

    return all_records
