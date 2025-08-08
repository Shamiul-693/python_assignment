# 📄 RAG Chatbot with PDF, DOCX, TXT, CSV, DB, and OCR Support

A Retrieval-Augmented Generation (RAG) chatbot built with **FastAPI** that can:
- 📂 Upload and parse various file types (PDF, DOCX, TXT, CSV, SQLite DB, and images via OCR)
- 🔍 Extract relevant text chunks and store embeddings in **FAISS**
- 💬 Answer user questions based only on uploaded documents
- 🧠 Use **LLM** to generate short, precise answers instead of dumping full text

---

## 🚀 Features
- **Multi-file type ingestion**: PDF, DOCX, TXT, CSV, SQLite DB, images with OCR.
- **Vector store**: Uses FAISS for fast similarity search.
- **Embedding generation**: Powered by SentenceTransformers or Ollama embeddings.
- **Question answering**: Retrieval + LLM prompt for context-aware answers.
- **Web UI**: Simple interface to upload files and ask questions.

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Shamiul-693/python_assignment.git
cd rag_api_project
```

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate.bat      # On Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Create `.env` file
```env
EMBEDDING_MODEL=all-MiniLM-L6-v2
VECTOR_STORE_PATH=vector_store/faiss_index
```

---

## ▶️ Running the Project

### Start FastAPI backend
```bash
uvicorn app.main:app --reload
python -m uvicorn app.main:app --reload
```

### Access API Docs
Open in browser:
```
http://127.0.0.1:8000/docs
```

---

## 📂 Folder Structure
```
rag_chatbot_project/
├── app/
│   ├── api/                # API endpoints
│   ├── ingestion/          # File parsers
│   ├── embeddings/         # Embedding and vector store logic
│   ├── query/              # Retrieval + QA logic
│   ├── utils/              # Helpers (OCR, etc.)
│   └── main.py              # FastAPI entrypoint
├── requirements.txt
├── .env
└── README.md
```

---

## 💡 How It Works
1. **Upload a file** → File is parsed into text.
2. **Text is split into chunks** → Each chunk is embedded and stored in FAISS.
3. **User asks a question** → The chatbot searches FAISS for relevant chunks.
4. **LLM generates a concise answer** → Uses retrieved chunks as context.

---

## 🖥 Example Usage
**Upload a PDF and ask a question:**
```
Question: "Give me the job experience from this PDF"
Answer:
1. Part-Time Teacher, Dhaka Polytechnic Institute — 2022–Present
2. Sub-Assistant Engineer, Small House Plan & Design — 2017–2022
3. Credit Risk Analyst, Palmpay Limited Bangladesh — Apr 2025–Present
```

---

## 🛠 Tech Stack
- **Backend**: FastAPI
- **Vector DB**: FAISS
- **Embeddings**: SentenceTransformers / Ollama
- **OCR**: pytesseract
- **LLM**: OpenAI API or local model

---
<img width="713" height="430" alt="image" src="https://github.com/user-attachments/assets/bba3168e-6a82-4133-9c20-b3f4a4580c3a" />


## 📜 License
This project is licensed under the MIT License.
