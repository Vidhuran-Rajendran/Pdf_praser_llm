from app.parser.pdf_parser import parse_pdf

# def process_pdf(file_path):
#     elements = parse_pdf(file_path)
    
#     return{"elements": elements}

def process_pdf(file_path):
    structured = parse_pdf(file_path)
    return structured
