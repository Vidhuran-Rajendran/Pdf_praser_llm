from app.parser.parser_router import parse_document
from app.parser.table_router import get_tables
from app.parser.cleaning_router import clean_all_tables

from app.schema.mapper import map_all_tables
from app.storage.db import insert_records


def process_pdf(file_path):
    parsed = parse_document(file_path)

    tables = get_tables(file_path, parsed)

    cleaned_tables = clean_all_tables(tables)

    # ✅ NEW STEP (CORE)
    records = map_all_tables(cleaned_tables)

    # ✅ store
    insert_records(records)

    return {
        "titles": parsed["titles"],
        "records": records
    }