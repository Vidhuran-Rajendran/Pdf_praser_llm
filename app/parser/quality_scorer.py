import pandas as pd


def get_table_metrics(df):

    rows, cols = df.shape

    total_cells = rows * cols

    populated = 0
    numeric = 0
    text = 0

    for row in df.values:

        for val in row:

            val = str(val).strip()

            if val.lower() in ["", "nan", "none"]:
                continue

            populated += 1

            if any(c.isdigit() for c in val):
                numeric += 1
            else:
                text += 1

    populated_ratio = (
        populated / total_cells
        if total_cells else 0
    )

    numeric_ratio = (
        numeric / populated
        if populated else 0
    )

    return {
        "rows": rows,
        "cols": cols,
        "populated_ratio": populated_ratio,
        "numeric_ratio": numeric_ratio
    }
def structural_score(df):

    m = get_table_metrics(df)

    score = 0

    # ✅ enough rows
    if m["rows"] >= 4:
        score += 0.25

    # ✅ enough cols
    if m["cols"] >= 2:
        score += 0.20

    # ✅ populated table
    if m["populated_ratio"] >= 0.30:
        score += 0.30

    # ✅ contains numeric structure
    if m["numeric_ratio"] >= 0.15:
        score += 0.25

    return round(score, 2)

def filter_useful_tables(tables):

    useful = []

    for t in tables:

        df = t["df"].copy()

        # ✅ normalize empty values
        df = df.map(
            lambda x: pd.NA
            if str(x).strip().lower()
            in ["nan", "none", ""]
            else x
        )

        # ✅ remove fully empty cols
        df = df.dropna(axis=1, how="all")

        # ✅ remove fully empty rows
        df = df.dropna(axis=0, how="all")

        rows, cols = df.shape

        # ✅ skip useless tables
        if rows <= 3:
            continue

        if cols <= 1:
            continue

        # ✅ update cleaned df
        t["df"] = df

        useful.append(t)

    return useful