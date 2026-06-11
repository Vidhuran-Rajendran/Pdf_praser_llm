import fitz
import os

def extract_images(pdf_path, base_output="images"):

    # ✅ create separate folder per PDF
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_folder = os.path.join(base_output, pdf_name)

    os.makedirs(output_folder, exist_ok=True)

    doc = fitz.open(pdf_path)
    images = []

    for page_num in range(len(doc)):

        page = doc[page_num]

        # ✅ render full page (better quality)
        pix_full = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        full_img_path = f"{output_folder}/page_{page_num}_full.png"
        pix_full.save(full_img_path)

        # ✅ detect blocks (layout based)
        blocks = page.get_text("blocks")

        for i, b in enumerate(blocks):

            x0, y0, x1, y1, text, *_ = b
            x0, y0, x1, y1 = map(float, (x0, y0, x1, y1))

            width = x1 - x0
            height = y1 - y0

            # ✅ relaxed filter (important)
            if width < 150 or height < 120:
                continue

            # ✅ remove noise (logos / random letters)
            if len(text.strip()) < 10:
                continue

            rect = fitz.Rect(x0, y0, x1, y1)

            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), clip=rect)

            img_path = f"{output_folder}/page_{page_num}_{i}.png"
            pix.save(img_path)

            images.append({
                "path": img_path,
                "page": page_num
            })

    return images