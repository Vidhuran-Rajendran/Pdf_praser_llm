from app.parser.parser_router import parse_document
from app.parser.table_router import get_tables
from app.parser.cleaning_router import clean_all_tables


def process_pdf(file_path):
    parsed = parse_document(file_path)

    tables = get_tables(file_path, parsed)

    # ✅ CLEAN STEP
    cleaned_tables = clean_all_tables(tables)

    return {
        "titles": parsed["titles"],
        "text": parsed["text"],
        "tables": cleaned_tables
    }