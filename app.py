from flask import Flask, render_template, request, session, jsonify
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = "genai123"


embeddings = OpenAIEmbeddings()


vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


prompt_template = """
You are My GenAI Chatbot, an intelligent AI assistant.

You help users learn about:
Artificial Intelligence
Machine Learning
Programming
Technology

If a user asks who you are, introduce yourself as:
"I am My GenAI Chatbot, an AI assistant that helps people learn AI and technology."

Use the provided context to answer the question.

Context:
{context}

Question:
{question}

Answer in simple plain text.
Do not use symbols like *, -, #, markdown, or bold text.
Use simple sentences and numbering if needed.
"""

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

# Retrieval QA chain with prompt
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    chain_type_kwargs={"prompt": PROMPT},
    return_source_documents=False
)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    if "messages" not in session:
        session["messages"] = []

    session["messages"].append({
        "role": "user",
        "content": user_message
    })

    # Identity response
    if user_message.lower() in ["who are you", "what are you", "introduce yourself"]:
        reply = "I am My GenAI Chatbot. I am an AI assistant that helps users learn Artificial Intelligence, Machine Learning, programming, and technology."

    else:
        rag_response = qa_chain.invoke({"query": user_message})
        reply = rag_response["result"]

    session["messages"].append({
        "role": "assistant",
        "content": reply
    })

    # Limit conversation history
    if len(session["messages"]) > 10:
        session["messages"] = session["messages"][-10:]

    session.modified = True

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)