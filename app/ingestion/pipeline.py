from app.parser.pdf_parser import parse_pdf
from app.parser.table_parser import extract_tables

def process_pdf(file_path):
    parsed = parse_pdf(file_path)

    tables = extract_tables(file_path)

    return {
        "titles": parsed["titles"],
        "text": parsed["text"],
        "tables": tables
    }