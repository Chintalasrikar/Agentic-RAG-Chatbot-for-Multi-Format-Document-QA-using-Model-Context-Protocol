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
  } ```
