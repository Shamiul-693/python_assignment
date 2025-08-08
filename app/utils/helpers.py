import os
import re

def split_text(text, max_length=500, overlap=50):
    """
    Splits text into overlapping chunks for embedding.
    """
    chunks = []
    start = 0
    text = re.sub(r'\s+', ' ', text.strip())  # Clean whitespace

    while start < len(text):
        end = start + max_length
        chunk = text[start:end]
        chunks.append(chunk)
        start += max_length - overlap

    return chunks

def allowed_file(filename):
    """
    Checks if file extension is supported.
    """
    ALLOWED_EXTENSIONS = ('.pdf', '.docx', '.txt', '.png', '.jpg', '.jpeg', '.csv', '.db')
    return filename.lower().endswith(ALLOWED_EXTENSIONS)

def get_file_extension(file_path):
    return os.path.splitext(file_path)[1].lower()
