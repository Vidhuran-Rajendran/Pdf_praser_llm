def clean_table(table):
    columns = table["columns"]
    rows = table["rows"]

    # remove empty columns
    valid_idx = [i for i, c in enumerate(columns) if c.strip() != ""]

    new_columns = [columns[i] for i in valid_idx]

    new_rows = []
    for r in rows:
        new_rows.append([r[i] for i in valid_idx if i < len(r)])

    # remove noisy rows (too small)
    filtered_rows = []
    for r in new_rows:
        if len([x for x in r if x.strip()]) >= 2:
            filtered_rows.append(r)

    return {
        "columns": new_columns,
        "rows": filtered_rows
    }


def clean_tables(tables):
    result = []

    for t in tables:
        cleaned = clean_table(t)

        # filter useless tables
        if len(cleaned["rows"]) >= 2:
            result.append(cleaned)

    return result
