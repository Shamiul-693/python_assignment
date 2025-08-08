# app/services/rag_engine.py

from transformers import pipeline

# Initialize the QA pipeline once
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def generate_answer(question: str, context: str) -> str:
    """
    Generate answer using HuggingFace QA pipeline.
    """
    try:
        result = qa_pipeline(question=question, context=context)
        return result['answer']
    except Exception as e:
        return f"Error generating answer: {str(e)}"


def answer_question(question: str, context: str) -> dict:
    """
    This function can be called from your API.
    It returns the answer along with the context.
    """
    answer = generate_answer(question, context)
    return {
        "context": context,
        "answer": answer
    }
