from app.services.rag_engine import answer_question

# Inside your /query endpoint, after getting relevant context:
response = answer_question(question=question, context=retrieved_context)

return response
