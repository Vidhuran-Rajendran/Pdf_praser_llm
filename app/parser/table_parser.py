from docling.document_converter import DocumentConverter

def extract_tables(file_path):
    converter = DocumentConverter()
    result = converter.convert(file_path)

    tables = []

    for table in result.document.tables:
        data = list(table.data)

        if not data or len(data) < 2:
            continue

        tables.append({
            "columns": data[0],
            "rows": data[1:]
        })

    return tables