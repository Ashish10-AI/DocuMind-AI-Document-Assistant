# 📄 DocuMind – AI Document Assistant

DocuMind is a simple AI-powered chatbot that lets you upload PDF documents and ask questions about their content. It uses **Retrieval Augmented Generation (RAG)** to search your documents and answer questions based only on what's inside them.

## ✨ Features

- Upload one or more PDF files
- Automatic text extraction, chunking, and embedding
- Ask questions in a chat interface and get context-aware answers
- Remembers conversation history during a session
- Built with an AI agent that decides when to search the documents

## 🛠️ Tech Stack

- **Streamlit** – web interface
- **LangChain / LangGraph** – RAG pipeline and agent orchestration
- **Groq (Llama 3.3 70B)** – language model for generating answers
- **HuggingFace Embeddings** (`all-MiniLM-L6-v2`) – converts text into vectors
- **InMemoryVectorStore** – stores and searches document embeddings
- **PyPDF** – PDF loading and parsing

## 📂 Project Structure

```
DocuMind-AI-Document-Assistant/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env                # API keys (not committed, see below)
├── .gitignore           
└── README.md
```

## ⚙️ Setup & Installation

**1. Clone the repository**
```bash
git clone https://github.com/bawa-mj/DocuMind-AI-Document-Assistant.git
cd DocuMind-AI-Document-Assistant
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add your API key**

Create a `.env` file in the project root and add your Groq API key:
```
GROQ_API_KEY=your_api_key_here
```
> Get a free API key from [console.groq.com](https://console.groq.com).

**5. Run the app**
```bash
streamlit run app.py
```

The app will open in your browser
## 📸 Screenshots

![Project Screenshot](https://github.com/bawa-mj/DocuMind-AI-Document-Assistant/blob/main/DocuMind%20%E2%80%93%20AI%20Document%20Assistant.png?raw=true)

