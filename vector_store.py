
from dotenv import load_dotenv
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

loader = PyPDFLoader("documents.pdf")
documents=loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings(
    api_key=os.getenv("OPENAI_API_KEY")
)

vectostore = FAISS.from_documents(docs,embeddings)
vectostore.save_local("faiss_index")

print("Vector database created successfully!")
