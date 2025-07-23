# Agentic-RAG-Chatbot-for-Multi-Format-Document-QA-using-Model-Context-Protocol

An agent-based Retrieval-Augmented Generation (RAG) chatbot that answers user questions based on multi-format uploaded documents. It leverages an **agentic architecture** and implements **Model Context Protocol (MCP)** for structured communication between agents.


## 🚀 Features

- ✅ **Multi-format Document Upload & Parsing**

- 🤖 **Agentic Architecture (3 Agents)**

    - **IngestionAgent**: Parses and preprocesses documents
 
    - **RetrievalAgent**: Performs embedding and semantic search
 
    - **LLMResponseAgent**: Formats query + context and calls LLM
 
- 🧩 **Model Context Protocol (MCP)**

- Implements structured message passing between agents  

  ```json
  {
    "sender": "RetrievalAgent",
    "receiver": "LLMResponseAgent",
    "type": "CONTEXT_RESPONSE",
    "trace_id": "abc-123",
    "payload": {
      "top_chunks": ["...", "..."],
      "query": "What are the KPIs?"
    }
  }

- 📚 **Vector Store + Embeddings**

  Uses **HuggingFace** or **OpenAI** embeddings with **FAISS** or **Chroma** for semantic retrieval

- 💬 **Interactive Chatbot UI**

  Built with **Streamlit** — allows:
  
  - 📁 Document upload  

  - 🔁 Multi-turn question answering  

  - 🧾 Display of answers with source context



## 🧰 Tech Stack

**LLM** : llama-3.3-70b-versatile (from Groq Cloud)

**Embeddings** : all-MiniLM-L6-v2

**Vector Store** : FAISS

**UI Framework** : Streamlit

**Protocol Laye** : Custom MCP (in-memory messaging)

**Language** : Python



## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Chintalasrikar/Agentic-RAG-Chatbot-for-Multi-Format-Document-QA-using-Model-Context-Protocol.git
cd Agentic-RAG-Chatbot-for-Multi-Format-Document-QA-using-Model-Context-Protocol
```

### 2. Install Requirements

```bash
pip install -r requirements.txt\
```

### 3. Run the App

```bash
streamlit run app.py
```

