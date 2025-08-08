import faiss
import numpy as np

class FaissVectorStore:
    def __init__(self, dim):
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.text_chunks = []

    def add_texts(self, texts, embeddings):
        self.index.add(np.array(embeddings).astype('float32'))
        self.text_chunks.extend(texts)

    def search(self, query_embedding, top_k=3):
        D, I = self.index.search(np.array([query_embedding]).astype('float32'), top_k)
        results = []
        for idx in I[0]:
            if idx < len(self.text_chunks):
                results.append(self.text_chunks[idx])
        return results
