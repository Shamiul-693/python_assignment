import streamlit as st
import requests
import base64

API_URL = "http://127.0.0.1:8000/api"

st.title("Smart RAG - Document QA")

st.header("Upload Document")
uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "txt", "csv", "db", "jpg", "png"])

if uploaded_file is not None:
    files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
    response = requests.post(f"{API_URL}/upload", files=files)
    if response.status_code == 200:
        st.success(f"Uploaded and processed: {uploaded_file.name}")
    else:
        st.error(f"Upload failed: {response.text}")

st.header("Ask a Question")
question = st.text_area("Enter your question here")

image_file = st.file_uploader("Or upload an image to ask about", type=["jpg", "png"])

if st.button("Get Answer"):
    data = {"question": question}
    if image_file:
        image_bytes = image_file.read()
        encoded_image = base64.b64encode(image_bytes).decode()
        data["image_base64"] = encoded_image

    response = requests.post(f"{API_URL}/query", json=data)
    if response.status_code == 200:
        answer_data = response.json()
        st.subheader("Answer")
        st.write(answer_data.get("answer", "No answer found."))
        st.subheader("Source Info")
        st.write(answer_data.get("source", {}))
    else:
        st.error(f"Query failed: {response.text}")
