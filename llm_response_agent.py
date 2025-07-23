from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    api_key=GROQ_API_KEY
)

# Generate response using Groq
def generate_response(query, top_chunks):
    context = "\n".join([chunk for chunk, _ in top_chunks])
    prompt = f"""You are an AI assistant for a Retrieval-Augmented Generation (RAG) chatbot. Your task is to answer user questions using only the information provided in the context. 
            Do not add external knowledge, opinions, or make assumptions beyond the given context. 
            If the context is insufficient to fully answer the question, acknowledge it and respond as accurately as possible based on what is available.
            Respond accurate, clear and detailed response, suitable for a chat interface.
            
            Context:\n{context}
            
            Question: {query}
            
            Answer:
            """
    
    # Call Groq LLM via LangChain
    try:
        response = llm.invoke(prompt)
        answer = response.content.strip()
    except Exception as e:
        print(f"Error calling Groq API: {str(e)}")
        return "Error generating response.", []

    sources = [doc_name for _, doc_name in top_chunks]
    return answer, sources