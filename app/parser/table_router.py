from app.config import MODE
from app.parser.table_parser import build_tables
from app.parser.gcp_table_parser import gcp_table_extract

def get_tables(file_path, parsed_data):
    if MODE == "paid":
        return gcp_table_extract(file_path)

    return build_tables(parsed_data["text"])