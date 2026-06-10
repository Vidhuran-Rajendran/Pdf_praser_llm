import fitz
import os


def extract_images(pdf_path, output_folder="images"):

    os.makedirs(output_folder, exist_ok=True)

    doc = fitz.open(pdf_path)
    images = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        img_list = page.get_images(full=True)

        for idx, img in enumerate(img_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            ext = base_image["ext"]
            file_name = f"{output_folder}/page_{page_num}_{idx}.{ext}"

            with open(file_name, "wb") as f:
                f.write(image_bytes)

            images.append({"path": file_name,"page": page_num})

    return images
