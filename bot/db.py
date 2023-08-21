from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
import os

os.environ["OPENAI_API_KEY"] = "sk-"

embedding = OpenAIEmbeddings()
persist_directory = '../db'


def create_db():
    documents = []
    loader = TextLoader('../data/return_policy.txt')
    documents.extend(loader.load())
    loader = TextLoader('../data/product_details.txt')
    documents.extend(loader.load())
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)

    embedding = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(documents=texts, embedding=embedding, persist_directory=persist_directory)
    return vectordb


def load_db():
    vectordb = None

    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)
    # qa = VectorDBQA.from_chain_type(llm=OpenAI(), chain_type="stuff", vectorstore=vectordb)
    return vectordb



# query = "how do i contact you"
# print(qa.run(query))
#
# query = "do you have tv?"
# print(qa.run(query))
