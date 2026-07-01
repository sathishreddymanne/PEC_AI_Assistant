# 🎓 PEC AI Assistant
### AI-Powered College Information Assistant using Retrieval-Augmented Generation (RAG)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![FAISS](https://img.shields.io/badge/Vector%20Database-FAISS-orange)
![Gemini](https://img.shields.io/badge/Google-Gemini-blueviolet)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 Overview

## 📖 Overview

PEC AI Assistant is an AI-powered chatbot developed to help students quickly access information about **Prathyusha Engineering College** through natural language conversations. The assistant leverages **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from official college documents and generate accurate, context-aware responses.

Unlike traditional chatbots that rely solely on a Large Language Model, this system first performs semantic search on a vector database to identify the most relevant document sections. The retrieved context is then combined with the user's query and processed by **Google Gemini**, ensuring reliable and document-grounded answers.

The project demonstrates the practical implementation of modern AI technologies, including **LangChain**, **FAISS**, **HuggingFace Embeddings**, and **Streamlit**, to build an intelligent document question-answering system. It is designed with a modular architecture, making it easy to scale by adding new PDFs without changing the application code.

This project showcases real-world applications of Large Language Models (LLMs), semantic search, vector databases, and Retrieval-Augmented Generation for educational and institutional knowledge management.

---

## ✨ Features

- 📄 Chat with multiple PDF documents
- 🤖 AI-powered responses using Google Gemini
- 🔍 Semantic Search using FAISS Vector Database
- 🧠 HuggingFace Embeddings
- 📑 Automatic PDF Chunking
- 💬 Interactive Streamlit Interface
- ⚡ Fast document retrieval
- 📚 Context-aware responses
- 🔒 Environment Variable support using `.env`
- 📁 Easily scalable to multiple documents

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Frontend | Streamlit |
| LLM | Google Gemini 2.5 Flash |
| Framework | LangChain |
| Embeddings | HuggingFace Sentence Transformers |
| Vector Database | FAISS |
| Document Loader | PyPDFLoader |
| Environment | Python Virtual Environment |

---

# 🏗 Project Architecture

```
                  PDF Documents
                        │
                        ▼
              PyPDFLoader (LangChain)
                        │
                        ▼
             Recursive Text Splitter
                        │
                        ▼
        HuggingFace Embedding Model
                        │
                        ▼
                FAISS Vector Store
                        │
─────────────────────────────────────────────
                 User Question
                        │
                        ▼
             Convert Question to Embedding
                        │
                        ▼
          Retrieve Relevant Chunks (FAISS)
                        │
                        ▼
             Prompt + Retrieved Context
                        │
                        ▼
                 Google Gemini LLM
                        │
                        ▼
                  Final AI Response
```

---

## 📂 Project Structure

```
PEC_AI_Assistant/
│
├── data/
│   ├── College_Brochure.pdf
│   └── Additional_Documents.pdf
│
├── vector_store/
│
├── ui.py
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── assets/
    ├── home.png
    ├── chatbot.png
    └── output.png
```

---

# ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/sathishreddymanne/PEC_AI_Assistant.git
```

```bash
cd PEC_AI_Assistant
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

---

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file inside the project directory.

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

---

# ▶ Run Application

```bash
streamlit run ui.py
```

---

# 💡 How It Works

### Step 1

Load one or more PDF documents.

↓

### Step 2

Split documents into smaller overlapping chunks.

↓

### Step 3

Generate vector embeddings using HuggingFace.

↓

### Step 4

Store embeddings in the FAISS Vector Database.

↓

### Step 5

Convert the user question into an embedding.

↓

### Step 6

Retrieve the most relevant document chunks.

↓

### Step 7

Pass retrieved context + question to Google Gemini.

↓

### Step 8

Generate an accurate response grounded in the documents.

---

# 📸 Screenshots

## Home Page

<img width="955" height="465" alt="Screenshot 2026-07-01 155408" src="https://github.com/user-attachments/assets/120615b0-a204-40e6-9cb1-3cfc7b571045" />



---

## Chat Interface

<img width="955" height="472" alt="Screenshot 2026-07-01 155513" src="https://github.com/user-attachments/assets/b17846c6-79f5-468e-bd4e-bf298178f281" />


---

## Generated Response

(<img width="955" height="472" alt="Screenshot 2026-07-01 155513" src="https://github.com/user-attachments/assets/9bd68b31-f0ac-418d-9ae2-21f905117da9" />
)

---

## code

<img width="959" height="566" alt="Screenshot 2026-07-01 162652" src="https://github.com/user-attachments/assets/a0533d45-e94b-49eb-bc2e-719e1620a0e4" />

)

---



# 🚀 Future Enhancements

- ✅ Multiple Document Support
- ✅ DOCX Support
- ✅ Excel Support
- ✅ Image OCR
- ✅ Voice-based Queries
- ✅ Chat History
- ✅ Authentication
- ✅ Cloud Deployment
- ✅ Automatic Document Updates
- ✅ Hybrid Search
- ✅ Citation Generation

---

# 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Retrieval-Augmented Generation (RAG)
- LangChain Framework
- Vector Databases (FAISS)
- HuggingFace Embeddings
- Prompt Engineering
- Google Gemini API
- Semantic Search
- Document Processing
- Streamlit Application Development

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

## Sathish Reddy Manne

**Final Year B.Tech (Artificial Intelligence & Machine Learning)**

Prathyusha Engineering College

GitHub:
https://github.com/sathishreddymanne

---

⭐ If you found this project useful, consider giving it a Star.
