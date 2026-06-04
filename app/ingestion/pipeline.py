from app.parser.page_builder import build_page_view
from app.parser.pdfplumber_table import extract_tables_pdf
from app.parser.table_normalizer import normalize_tables
from app.parser.quality_scorer import filter_useful_tables
from app.embeddings.chunker import dataframe_to_chunks
from app.embeddings.vectordb import store_chunks


def process_pdf(file_path):

    pages = build_page_view(file_path)
    raw_tables = extract_tables_pdf(file_path)
    normalized_tables = normalize_tables(raw_tables)
    useful_tables = filter_useful_tables(normalized_tables)
    
    all_chunks = []
    for table in useful_tables:
        chunks = dataframe_to_chunks(table)
        all_chunks.extend(chunks)
    store_chunks(all_chunks)

    return {
        "pages": pages,
        "tables": useful_tables,
        "chunks": all_chunks
    }
