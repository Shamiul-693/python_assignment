from sentence_transformers import SentenceTransformer

# Load model once (free and offline)
model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_texts(texts):
    # texts: List[str]
    return model.encode(texts, show_progress_bar=False)
