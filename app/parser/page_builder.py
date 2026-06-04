import fitz
import pdfplumber


def build_page_view(file_path):
    doc = fitz.open(file_path)
    pages_output = []

    with pdfplumber.open(file_path) as pdf:

        for i in range(doc.page_count):
            page = doc.load_page(i)
            page_dict = {
                "page": i,
                "content": []
            }

            
            # ✅ TEXT
            content = page.get_text()
            text_lines = str(page.get_text("text") or "").splitlines()


            for line in text_lines:
                line = line.strip()

                if line:
                    page_dict["content"].append({
                        "type": "text",
                        "value": line
                    })


            # ✅ TABLES
            plumber_page = pdf.pages[i]
            raw_tables = plumber_page.extract_tables()

            for table in raw_tables:
                cleaned = []

                for row in table:
                    r = [cell for cell in row if cell not in (None, "", " ")]
                    if len(r) >= 2:
                        cleaned.append(r)

                if len(cleaned) >= 2:
                    page_dict["content"].append({
                        "type": "table",
                        "value": cleaned
                    })

            pages_output.append(page_dict)

    return pages_output
