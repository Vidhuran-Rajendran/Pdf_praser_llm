from app.config import MODE
from app.parser.pdfplumber_table import extract_tables_pdf
from app.parser.gcp_table_parser import gcp_table_extract


def get_tables(file_path, parsed):
    if MODE == "paid":
        return gcp_table_extract(file_path)

    return extract_tables_pdf(file_path)