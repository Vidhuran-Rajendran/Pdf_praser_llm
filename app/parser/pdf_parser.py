from unstructured.partition.pdf import partition_pdf

def parse_pdf(file_path):
    elements = partition_pdf(filename=file_path)

    structured = {
        "titles": [],
        "text": [],
        "tables": []
    }

    for el in elements:
        text = el.text if hasattr(el, "text") else ""

        if "Table" in str(type(el)):
            structured["tables"].append(text)
        elif "Title" in str(type(el)):
            structured["titles"].append(text)
        else:
            structured["text"].append(text)

    return structured