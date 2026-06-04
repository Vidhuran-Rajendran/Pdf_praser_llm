import fitz  # PyMuPDF


def parse_pymupdf(file_path):
    doc = fitz.open(file_path)

    titles = []
    text = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        content = page.get_text()

        if not content:
            continue

        lines = content.split("\n") if isinstance(content, str) else []

        for line in lines:
            line = line.strip()

            if not line:
                continue

            # ✅ Title detection (important)
            if (
                line.isupper() or
                "TEST REPORT" in line or
                "BRAKE" in line
            ):
                titles.append(line)
            else:
                text.append(line)

    return {
        "titles": titles,
        "text": text
    }
