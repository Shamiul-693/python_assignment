from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import os
import shutil

from app.services.document_loader import load_pdf_text_chunks
from app.services.embeddings import embed_texts, model
from app.services.vector_store import FaissVectorStore

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

# Initialize vector store and keep it in memory for demo
vector_store = None

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    global vector_store
    filepath = os.path.join(DATA_DIR, file.filename)
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Load and embed chunks
    chunks = load_pdf_text_chunks(filepath)
    embeddings = embed_texts(chunks)

    # Create or reset FAISS index
    vector_store = FaissVectorStore(dim=embeddings[0].shape[0])
    vector_store.add_texts(chunks, embeddings)

    return {"filename": file.filename, "message": "File uploaded and processed successfully."}

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
async def query_endpoint(query: QueryRequest):
    if vector_store is None:
        return JSONResponse(status_code=400, content={"error": "No documents uploaded yet."})

    # Embed the question
    question_embedding = embed_texts([query.question])[0]

    # Search top 3 chunks
    relevant_chunks = vector_store.search(question_embedding, top_k=3)

    # Simple concatenation of relevant context (for demo)
    context = "\n---\n".join(relevant_chunks)

    # For demo, answer = return context + question (replace with actual LLM in real app)
    answer = f"Context:\n{context}\n\nAnswer to your question: {query.question}"

    return {"question": query.question, "answer": answer}
