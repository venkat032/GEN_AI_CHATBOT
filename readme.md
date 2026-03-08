# GenAI RAG Chatbot 🤖

This project is a **Retrieval Augmented Generation (RAG) AI Chatbot** built using **Flask, LangChain, FAISS, and OpenAI**.
The chatbot can answer questions using information from a custom **PDF knowledge base**.

It combines **vector search** with a **large language model** to generate intelligent responses.

---

## Features

* AI powered chatbot interface
* Retrieval Augmented Generation (RAG) architecture
* Answers questions from a custom PDF document
* Vector database using FAISS
* LangChain integration with OpenAI
* Modern chatbot UI built with HTML and CSS
* Secure API key management using `.env`

---

## Project Architecture

User Question
↓
Flask API
↓
LangChain Retriever
↓
FAISS Vector Database
↓
OpenAI GPT Model
↓
Generated Answer

---

## Project Structure

GEN_AI_CHATBOT
│
├── app.py                 # Flask backend for chatbot
├── vector_store.py        # Creates FAISS vector database from PDF
├── documents.pdf          # Knowledge base document
├── requirements.txt       # Project dependencies
├── .gitignore             # Ignore sensitive files
├── README.md              # Project documentation
│
└── templates
  └── index.html          # Chatbot user interface

---

## Installation

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/genai-rag-chatbot.git

cd genai-rag-chatbot

---

### 2. Install dependencies

pip install -r requirements.txt

---

### 3. Add OpenAI API Key

Create a `.env` file in the project root.

OPENAI_API_KEY=your_openai_api_key_here

---

### 4. Create Vector Database

Run the following command to generate the FAISS vector database from the PDF document.

python vector_store.py

This will create a folder:

faiss_index/

---

### 5. Run the Chatbot

python app.py

Open your browser and go to:

http://127.0.0.1:8000

---

## Example Questions

You can ask questions like:

What is Artificial Intelligence?
Explain the AI engineer roadmap
How can I become an AI engineer?
What skills are required for machine learning?

---

## Technologies Used

Python
Flask
LangChain
OpenAI API
FAISS Vector Database
HTML and CSS

---

## Security

The `.env` file is excluded from the repository using `.gitignore` to keep API keys secure.

---

## Future Improvements

Add conversation memory
Support multiple documents
Add streaming responses like ChatGPT
Deploy the chatbot using Docker or cloud platforms

---

## Author

Venkat Narayana

AI / Machine Learning Developer
