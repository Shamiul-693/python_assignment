import os
from PyPDF2 import PdfReader

def load_pdf_text_chunks(filepath, chunk_size=500, chunk_overlap=50):
    reader = PdfReader(filepath)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() + "\n"
    # Split text into overlapping chunks
    chunks = []
    start = 0
    while start < len(full_text):
        end = min(start + chunk_size, len(full_text))
        chunk = full_text[start:end]
        chunks.append(chunk)
        start += chunk_size - chunk_overlap
    return chunks
