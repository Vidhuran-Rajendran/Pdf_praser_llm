import easyocr

# ✅ load once
reader = easyocr.Reader(['en'], gpu=False)


def extract_text_from_image(image_path):

    result = reader.readtext(image_path)

    text_blocks = [r["text"] if isinstance(r, dict) else r[1] for r in result]

    return " ".join(text_blocks)
