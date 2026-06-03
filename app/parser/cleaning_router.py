from app.config import MODE
from app.parser.table_cleaner import clean_tables
from app.parser.gcp_table_cleaner import clean_gcp_tables

def clean_all_tables(tables):
    if MODE == "paid":
        return clean_gcp_tables(tables)

    return clean_tables(tables)