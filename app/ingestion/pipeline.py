import os
from collections import Counter
from app.parser.page_builder import build_page_view
from app.parser.pdfplumber_table import extract_tables_pdf
from app.parser.table_normalizer import normalize_tables
from app.parser.quality_scorer import filter_useful_tables
from app.embeddings.chunker import dataframe_to_chunks,chunk_text_pages
from app.embeddings.vectordb import store_chunks
from app.storage.duckdb_store import initialize_db,insert_chunks
from app.parser.camelot_parser import extract_tables_camelot
from app.parser.image_extractor import extract_images
from app.embeddings.image_processor import extract_text_from_image



def process_pdf(file_path):

    pages = build_page_view(file_path)
    project_name = extract_project_name(pages)
    print(f"✅ Project detected: {project_name}")
    dvp_text = extract_dvp_text(pages, file_path)
    raw_tables = extract_tables_camelot(file_path)
    normalized_tables = normalize_tables(raw_tables)
    useful_tables = filter_useful_tables(normalized_tables)
    images = extract_images(file_path)
    
    all_chunks = []
    image_chunks = []

    for img in images:
        
        ocr_text = extract_text_from_image(img["path"])

        # ✅ extract title (first line usually)
        lines = ocr_text.split("\n")
        title = lines[0] if lines else "unknown graph"

        TEXT = f"""
        Graph Title: {title}

        {dvp_text}
        Project: {project_name}

        Data:
        {ocr_text}
        """


        
        chunk = {
                "id": f"image_{img['page']}_{len(image_chunks)}",
                "text": TEXT,
                "metadata": {
                    "page": img["page"],
                    "project": project_name,
                    "dvp_text": dvp_text,
                    "doc_id": file_path,
                    "pdf_name": os.path.basename(file_path),
                    "image_path": img["path"],
                    "graph_title": title,
                    "source": "image"
                }
            }

        image_chunks.append(chunk)

    
    for table in useful_tables:
        chunks = dataframe_to_chunks(table,file_path)        
        for c in chunks:
            c["metadata"]["project"] = project_name
            c["metadata"]["dvp_text"] = dvp_text            
            c["metadata"]["pdf_name"] = os.path.basename(file_path)
            c["metadata"]["doc_id"] = file_path

        all_chunks.extend(chunks)
    text_chunks = chunk_text_pages(pages)
    
    for t in text_chunks:
        t["metadata"]["project"] = project_name
        t["metadata"]["dvp_text"] = dvp_text
        t["metadata"]["pdf_name"] = os.path.basename(file_path)
        t["metadata"]["doc_id"] = file_path

    combined_chunks = all_chunks + text_chunks + image_chunks

    store_chunks(combined_chunks)
    
    initialize_db()
    insert_chunks(combined_chunks)

    return {
        "pages": pages,
        "tables": useful_tables,
        "chunks": all_chunks
    }



def extract_project_name(pages):
    for page in pages[:5]:
        for item in page["content"]:
            if item["type"] == "text":
                line = item["value"]

                if "project no" in line.lower():
                    import re
                    match = re.search(
                        r"project\s*no\s*[:\-]?\s*([A-Z0-9\-]+)",
                        line, re.IGNORECASE
                    )
                    if match:
                        return match.group(1).upper()

    return "UNKNOWN_PROJECT"


def extract_dvp_text(pages, file_path):

    for item in pages[0]["content"]:
        if item["type"] == "text":
            line = item["value"]

            if "evaluation" in line.lower() or "test" in line.lower():
                return line.strip()
