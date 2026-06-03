from docling.document_converter import DocumentConverter

def extract_tables(file_path):
    converter = DocumentConverter()
    result  = converter.convert(file_path)