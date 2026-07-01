from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def load_pdf(folder_path):
    loader = PyPDFDirectoryLoader(folder_path)
    documents = loader.load()
    return documents


def split_documents(documents, chunk_size=2000, chunk_overlap=400):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = splitter.split_documents(documents)
    return chunks

def load_embedding_model():
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return embedding_model


def create_vector_store(chunks, embedding_model):
    vector_store = FAISS.from_documents(
        chunks,
        embedding_model
    )
    return vector_store

def save_vector_store(vector_store, folder_path="faiss_index"):
    vector_store.save_local(folder_path)

if __name__ == "__main__":

    documents = load_pdf("data")

    chunks = split_documents(documents)

    embedding_model = load_embedding_model()

    vector_store = create_vector_store(
        chunks,
        embedding_model
    )

    save_vector_store(
        vector_store,
        "vectorstore"
    )

    print("✅ Vector Store Created Successfully!")    