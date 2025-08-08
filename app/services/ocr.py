import pytesseract
from PIL import Image

def extract_text_from_image(image_path: str) -> str:
    """
    Extracts text from an image file using Tesseract OCR.
    """
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='eng')
    return text
