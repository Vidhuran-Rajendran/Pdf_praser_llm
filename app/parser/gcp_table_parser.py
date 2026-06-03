from google.cloud import documentai

def gcp_table_extract(file_path):
    # Replace these with your values
    project_id = "YOUR_PROJECT_ID"
    location = "us"
    processor_id = "YOUR_PROCESSOR_ID"

    client = documentai.DocumentProcessorServiceClient()

    name = f"projects/{project_id}/locations/{location}/processors/{processor_id}"

    with open(file_path, "rb") as f:
        file_content = f.read()

    request = documentai.ProcessRequest(
        name=name,
        raw_document=documentai.RawDocument(
            content=file_content,
            mime_type="application/pdf"
        )
    )

    result = client.process_document(request=request)
    doc = result.document

    tables = []

    for page in doc.pages:
        for table in page.tables:
            rows = []
            for row in table.body_rows:
                r = []
                for cell in row.cells:
                    r.append(cell.layout.text_anchor.content.strip())
                rows.append(r)

            if rows:
                tables.append({
                    "columns": rows[0],
                    "rows": rows[1:]
                })

    return tables
