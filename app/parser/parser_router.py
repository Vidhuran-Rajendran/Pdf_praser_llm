from app.config import MODE
from app.parser.unstructured_parser import parse_unstructured
from app.parser.gcp_parser import parse_gcp

def parse_document(file_path):
    if MODE == "paid":
        return parse_gcp(file_path)

    return parse_unstructured(file_path)
