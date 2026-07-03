from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")




llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)


def load_embedding_model():
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return embedding_model

def load_vector_store(folder_path, embedding_model):
    vector_store = FAISS.load_local(
        folder_path,
        embedding_model,
        allow_dangerous_deserialization=True
    )
    return vector_store

def create_retriever(vector_store, k=10):
    retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={
        "k": 10,
        
    }
)
    return retriever

def create_prompt():
    prompt = ChatPromptTemplate.from_template("""


You are an AI assistant for Prathyusha Engineering College.

Answer  from the provided context and also give answers for for general questions and any questions from internet 

If the answer is present in multiple chunks, combine the information into one complete answer.

Do not say "not explicitly mentioned" unless you have carefully checked all retrieved context.



Previous Conversation:
{chat_history}

Context:
{context}

Question:
{question}

Answer:
""")


    return prompt


def format_docs(docs):
    return "\n\n".join(
        doc.page_content for doc in docs

    )

def create_rag_chain(retriever, prompt, llm):
    rag_chain = (
        {
            "context": lambda x: format_docs(

                retriever.invoke(x["question"])

            ),
            "question": lambda x: x["question"],
            "chat_history": lambda x: x["chat_history"],

        }

        | prompt

        | llm

        | StrOutputParser()

    )
    return rag_chain
print("Vector Store Created Successfully!")
def load_rag_chain():

    embedding_model = load_embedding_model()

    vector_store = load_vector_store(
        "vectorstore",
        embedding_model
    )

    retriever = create_retriever(vector_store)

    prompt = create_prompt()

    rag_chain = create_rag_chain(
        retriever,
        prompt,
        llm
    )

    return rag_chain

if __name__ == "__main__":

    rag_chain = load_rag_chain()

    chat_history = ""

    while True:

        question = input(
            "\nAsk a question about Prathyusha Engineering College (type 'exit' to quit): "
        )

        if question.lower() == "exit":
            print("Goodbye!")
            break

        docs = retriever.invoke(question)

        print("\n" + "=" * 80)
        print("Retrieved Chunks")
        print("=" * 80)

        for i, doc in enumerate(docs):
            print(f"\n----- Chunk {i+1} -----\n")
            print(doc.page_content[:500])   
            print()

        response = rag_chain.invoke({
            "question": question,
            "chat_history": chat_history
        })
        print("\nAnswer:\n")
        print(response)

        chat_history += f"\nUser: {question}\nAssistant: {response}"