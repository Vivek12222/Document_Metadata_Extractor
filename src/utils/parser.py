from docx import Document
from PIL import Image
import pytesseract

def extract_text_docx(path):
    doc = Document(path)
    return "\n".join([p.text for p in doc.paragraphs])

def extract_text_image(path):
    image = Image.open(path)
    return pytesseract.image_to_string(image)
