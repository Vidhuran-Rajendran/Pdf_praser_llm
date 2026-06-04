import pdfplumber


def clean_row(row):
    # ✅ remove None / empty cells
    return [cell for cell in row if cell not in (None, "", " ")]


def normalize_table(table):
    max_len = max(len(r) for r in table)

    normalized = []
    for r in table:
        r = r + [""] * (max_len - len(r))
        normalized.append(r)

    return normalized


def extract_tables_pdf(file_path):
    tables = []

    with pdfplumber.open(file_path) as pdf:
        for page_num, page in enumerate(pdf.pages):

            raw_tables = page.extract_tables()

            if not raw_tables:
                continue

            for table in raw_tables:

                cleaned_table = []

                for row in table:
                    cleaned = clean_row(row)

                    # ✅ keep only meaningful rows
                    if len(cleaned) >= 2:
                        cleaned_table.append(cleaned)

                if len(cleaned_table) < 2:
                    continue

                # ✅ fix alignment
                normalized = normalize_table(cleaned_table)

                columns = normalized[0]
                rows = normalized[1:]

                tables.append({
                    "columns": columns,
                    "rows": rows,
                    "page": page_num
                })

                print(f"✅ Table extracted from page {page_num}")

    return tables