from mcp import send_mcp_message
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Initialize embedder and vector store
embedder = SentenceTransformer("all-MiniLM-L6-v2")
index = None
chunks = []
document_names = []

# Store embeddings in FAISS
def store_embeddings(chunks_in, document_name):
    global index, chunks, document_names
    embeddings = embedder.encode(chunks_in, convert_to_numpy=True)
    if index is None:
        dimension = embeddings.shape[1]
        index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    chunks.extend(chunks_in)
    document_names.extend([document_name] * len(chunks_in))

# Retrieve relevant chunks
def retrieve_chunks(query, k=3):
    query_embedding = embedder.encode([query], convert_to_numpy=True)
    distances, indices = index.search(query_embedding, k)
    top_chunks = [(chunks[i], document_names[i]) for i in indices[0]]
    send_mcp_message(
        "RetrievalAgent", "LLMResponseAgent", "CONTEXT_RESPONSE",
        {"top_chunks": top_chunks, "query": query}
    )
    return top_chunks