# 📄 DocuMind — AI Document Assistant

**Chat with your PDFs using AI. Get context-aware answers grounded in your documents.**

DocuMind is an AI-powered document assistant that lets you upload PDF files and ask questions about their content using natural language. Built with **Retrieval-Augmented Generation (RAG)**, it retrieves relevant information from your documents and uses a large language model to generate meaningful, context-aware answers.

Instead of manually searching through lengthy documents, DocuMind helps you find information faster through an interactive chat interface.

## ✨ Features

* 📁 **PDF Upload** — Upload one or more PDF documents for analysis.
* 🔍 **Automatic Text Processing** — Extracts text, splits it into chunks, and generates embeddings for semantic retrieval.
* 💬 **Conversational Q&A** — Ask questions about your uploaded documents in natural language.
* 🧠 **Retrieval-Augmented Generation (RAG)** — Generates answers using relevant document context.
* 🤖 **AI Agent Workflow** — Uses LangGraph-based orchestration to determine when document retrieval is needed.
* 📚 **Semantic Search** — Finds relevant document passages using vector embeddings.
* 🔄 **Conversation Memory** — Maintains conversation history during the current session.
* ⚡ **Interactive Web Interface** — Built with Streamlit for a simple and accessible user experience.

## 🛠️ Tech Stack

| Technology                         | Purpose                                  |
| ---------------------------------- | ---------------------------------------- |
| Python                             | Core application logic                   |
| Streamlit                          | Interactive web interface                |
| LangChain                          | Document processing and LLM integration  |
| LangGraph                          | AI agent workflow orchestration          |
| Groq API                           | LLM inference using Llama 3.3 70B        |
| Hugging Face Sentence Transformers | Text embeddings using `all-MiniLM-L6-v2` |
| InMemoryVectorStore                | Vector storage and semantic retrieval    |
| PyPDF                              | PDF loading and text extraction          |

## 🧠 How It Works

DocuMind follows a Retrieval-Augmented Generation workflow to answer questions using the contents of uploaded documents.

```text
       Upload PDF Documents
                |
                v
        Extract PDF Text
                |
                v
         Split into Chunks
                |
                v
       Generate Embeddings
                |
                v
      Store in Vector Store
                |
                v
         Ask a Question
                |
                v
       Retrieve Relevant Text
                |
                v
       LLM Generates Answer
                |
                v
      Context-Aware Response
```

### Workflow Overview

1. **Document Upload:** The user uploads one or more PDF files.
2. **Text Extraction:** PyPDF extracts readable text from the documents.
3. **Text Chunking:** The extracted content is divided into smaller sections for retrieval.
4. **Embedding Generation:** Hugging Face embeddings convert text chunks into vector representations.
5. **Context Retrieval:** Relevant document sections are retrieved from the in-memory vector store when needed.
6. **Answer Generation:** The Groq-hosted Llama 3.3 70B model generates a response using the retrieved context.
7. **Conversation:** Users can ask follow-up questions while conversation history is maintained during the session.

## 🏗️ Project Structure

```text
DocuMind-AI-Document-Assistant/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

## 🚀 Getting Started

Follow these steps to run DocuMind locally.

### Prerequisites

* Python 3.10 or a compatible version required by your dependencies
* pip
* A Groq API key

### 1. Clone the Repository

```bash
git clone https://github.com/Ashish10-AI/DocuMind-AI-Document-Assistant.git
cd DocuMind-AI-Document-Assistant
```

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from the [Groq Console](https://console.groq.com/).

**Important:** Keep your API key private. Never commit your `.env` file or expose your credentials in public repositories.

### 5. Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, usually `http://localhost:8501`.

## 💡 Example Use Cases

DocuMind can be useful for:

* 📚 **Students:** Understand study materials, notes, and academic PDFs.
* 🔬 **Researchers:** Explore research papers and retrieve relevant information.
* 💼 **Professionals:** Find specific details in reports and documentation.
* 📑 **Document Analysis:** Ask questions about lengthy documents without manually searching every page.
* 📝 **Learning and Revision:** Summarize or clarify information through follow-up questions.

## 🔑 Why RAG?

A conventional LLM may answer questions using general knowledge rather than the contents of a specific document.

Retrieval-Augmented Generation helps address this limitation by retrieving relevant document passages and supplying them as context to the language model before it generates an answer.

This makes responses more relevant to the uploaded material. However, answers can still be incorrect or incomplete, so important information should be verified against the original document.

## ⚠️ Limitations

* The current application is designed for PDF documents.
* The in-memory vector store is temporary; indexed document data is not guaranteed to persist between application sessions.
* Conversation history is maintained during the current session.
* Document quality and answer accuracy depend on the extracted text, retrieved context, and language model.
* Scanned PDFs may require OCR support to extract text reliably.
* Groq API access and usage are subject to the provider's availability and limits.

## 🔮 Future Improvements

Potential improvements include:

* [ ] Support for DOCX, TXT, and additional file formats.
* [ ] Persistent vector storage for reusable document indexes.
* [ ] Source citations linking answers to specific pages or passages.
* [ ] Chat history persistence across sessions.
* [ ] OCR support for scanned PDFs.
* [ ] Improved document retrieval and answer evaluation.
* [ ] Document summarization and structured information extraction.
* [ ] Deployment as a publicly accessible web application.

## 🎯 Key Learning Outcomes

This project demonstrates practical experience with:

* Retrieval-Augmented Generation (RAG)
* Semantic search and vector embeddings
* PDF parsing and document preprocessing
* Large Language Model (LLM) integration
* LangChain and LangGraph
* AI agent workflow orchestration
* Building interactive AI applications with Streamlit

## 👨‍💻 Author

**Ashish Yadav**

* GitHub: [@Ashish10-AI](https://github.com/Ashish10-AI)
* LinkedIn: [Ashish Yadav](https://www.linkedin.com/in/ashish-yadav-ai/)

---

⭐ If you find this project interesting, consider giving the repository a star!

*Built to make document understanding faster, simpler, and more interactive with AI.*
