from app.parser.page_builder import build_page_view

def process_pdf(file_path):
    pages = build_page_view(file_path)

    return {
        "pages": pages
    }