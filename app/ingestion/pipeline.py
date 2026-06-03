from app.parser.parser_router import parse_document
from app.parser.table_router import get_tables

def process_pdf(file_path):
    parsed = parse_document(file_path)

    tables = get_tables(file_path, parsed)

    return {
        "titles": parsed["titles"],
        "text": parsed["text"],
        "tables": tables
    }
