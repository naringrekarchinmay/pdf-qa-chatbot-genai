📄 PDF QA Chatbot (RAG Demo)

A Python-based PDF Question–Answering chatbot built to understand and demonstrate the core concepts behind Retrieval-Augmented Generation (RAG).
This project allows users to upload a PDF document and ask natural language questions, with answers generated strictly from the document content.

🚀 Project Overview

Large Language Models (LLMs) do not inherently “know” the content of private documents.
This project demonstrates how GenAI systems reason over documents by combining:

Document chunking

Embeddings

Vector similarity search

Context-aware prompting

LLM-based answer generation

The result is a simple but complete end-to-end RAG pipeline.

🧠 What This Project Demonstrates

📄 PDF ingestion and text extraction

✂️ Text chunking with overlap

🔢 Embedding generation

🧠 Vector storage using FAISS

🔍 Similarity-based retrieval

💬 Context-injected LLM prompting

🧾 Answers grounded in document content (no hallucination)

This project was built as part of an Introduction to Generative AI learning journey to understand how modern document-based QA systems work under the hood.
```
🗂 Project Structure
pdf-qa-chatbot-genai/
│
├── chatbot.py          # Main Streamlit application
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

🔄 How the System Works (High-Level Flow)

1️⃣ User uploads a PDF document
2️⃣ Text is extracted from all pages
3️⃣ Text is split into overlapping chunks
4️⃣ Each chunk is converted into vector embeddings
5️⃣ Embeddings are stored in a FAISS vector database
6️⃣ User asks a question
7️⃣ Most relevant chunks are retrieved via similarity search
8️⃣ Retrieved context is passed to the LLM
9️⃣ LLM generates an answer grounded in the document

🛠 Tech Stack

Python

Streamlit

LangChain

FAISS

OpenAI / Chat LLM

PyPDF2

▶️ How to Run Locally
1️⃣ Clone the repository

```
git clone https://github.com/naringrekarchinmay/pdf-qa-chatbot-genai.git
cd pdf-qa-chatbot-genai
```
2️⃣ Install dependencies
```
pip install -r requirements.txt
```
3️⃣ Set your API key
```
 export OPENAI_API_KEY="your-api-key"

```



4️⃣ Run the app

```
streamlit run chatbot.py
```
🎯 Learning Outcomes

Through this project, I gained hands-on understanding of:

How LLMs interact with external knowledge

Why chunking and overlap matter

How embeddings enable semantic search

How vector databases power document retrieval

How RAG reduces hallucination in GenAI systems

🔮 Future Improvements

Multi-document support

Source citation highlighting

Improved chunking strategies

Persistent vector storage

UI enhancements

Integration with more advanced LLMs

📬 About

This project was built as part of my Generative AI learning journey to strengthen my understanding of modern AI-powered document retrieval systems.

Feel free to explore, fork, or provide feedback!
