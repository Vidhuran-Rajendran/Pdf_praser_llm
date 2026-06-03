import re

def is_table_line(line):
    nums = re.findall(r"\d+\.?\d*", line)
    return len(nums) >= 2


def extract_raw_tables(text_lines):
    tables = []
    current = []

    for line in text_lines:
        line = line.strip()

        if is_table_line(line):
            current.append(line)
        else:
            if len(current) >= 3:
                tables.append(current)
            current = []

    if len(current) >= 3:
        tables.append(current)

    return tables


def split_row(line):
    parts = re.split(r"\s{2,}", line)
    if len(parts) <= 1:
        parts = line.split()

    return [p.strip() for p in parts if p.strip()]


def structure_table(lines):
    rows = [split_row(l) for l in lines]

    max_len = max(len(r) for r in rows)

    norm = []
    for r in rows:
        if len(r) < max_len:
            r += [""] * (max_len - len(r))
        norm.append(r)

    return {
        "columns": norm[0],
        "rows": norm[1:]
    }


def build_tables(text_lines):
    raw_tables = extract_raw_tables(text_lines)

    result = []
    for t in raw_tables:
        structured = structure_table(t)

        if len(structured["rows"]) >= 2:
            result.append(structured)

    return result