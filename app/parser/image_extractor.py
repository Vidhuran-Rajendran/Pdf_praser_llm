import fitz
import os

def extract_images(pdf_path, output_folder="images"):

    os.makedirs(output_folder, exist_ok=True)

    doc = fitz.open(pdf_path)
    images = []

    for page_num in range(len(doc)):

        page = doc[page_num]

        # ✅ use get_images instead of text blocks
        img_list = page.get_images(full=True)

        for idx, img in enumerate(img_list):

            xref = img[0]

            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            ext = base_image["ext"]

            width = img[2]
            height = img[3]

            # ✅ filter unwanted images (logos / icons)
            if width < 300 or height < 200:
                continue

            img_path = f"{output_folder}/page_{page_num}_{idx}.{ext}"

            with open(img_path, "wb") as f:
                f.write(image_bytes)

            images.append({
                "path": img_path,
                "page": page_num,
                "width": width,
                "height": height
            })

    return images