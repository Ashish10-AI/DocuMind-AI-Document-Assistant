from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_community.vectorstores import InMemoryVectorStore
from langchain.agents import create_agent
from langchain.tools import tool
from langgraph.checkpoint.memory import InMemorySaver


st.set_page_config(
    page_title="DocuMind",
    page_icon="📄",
    layout="centered"
)


# Basic CSS - just to make text readable on mobile, nothing fancy
st.markdown("""
<style>

.block-container {
    max-width: 800px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

[data-testid="stChatMessageContent"] {
    overflow-wrap: anywhere;
    word-break: break-word;
}

@media (max-width: 600px) {

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    h1 {
        font-size: 1.4rem !important;
    }

    [data-testid="stChatMessageContent"] {
        font-size: 0.95rem;
        line-height: 1.5;
    }

    .stButton button {
        width: 100%;
    }

}

</style>
""", unsafe_allow_html=True)


if "document_uploaded" not in st.session_state:
    st.session_state.document_uploaded = False

if "agent" not in st.session_state:
    st.session_state.agent = None

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "messages" not in st.session_state:
    st.session_state.messages = []


def process_document(path):

    loader = PyPDFDirectoryLoader(path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    docs = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_db = InMemoryVectorStore.from_documents(
        documents=docs,
        embedding=embeddings
    )

    st.session_state.vector_store = vector_db

    llm = ChatGroq(
        model="llama-3.3-70b-versatile"
    )

    @tool
    def retrieve_context(query: str):
        """Retrieve relevant information from uploaded documents."""

        docs = vector_db.similarity_search(
            query=query,
            k=3
        )

        context = ""

        for doc in docs:
            context += doc.page_content + "\n\n"

        return context

    system_prompt = """
    You are a helpful assistant that answers questions using retrieved context.

    The knowledge base contains information from the uploaded documents.

    Use the retrieve_context tool when the question is related to the uploaded documents.

    Answer based on the retrieved context.

    If the answer is not available in the documents, say you don't know.
    """

    memory = InMemorySaver()

    agent = create_agent(
        model=llm,
        tools=[retrieve_context],
        system_prompt=system_prompt,
        checkpointer=memory
    )

    st.session_state.agent = agent
    st.session_state.document_uploaded = True


st.title("📄 DocuMind")

st.caption("AI Document Assistant • Upload PDFs and ask questions")


if not st.session_state.document_uploaded:

    uploaded = st.file_uploader(
        "Upload your PDF",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded:

        with st.spinner("Processing documents..."):

            path = "./doc_files/"

            os.makedirs(path, exist_ok=True)

            for file in uploaded:

                file_path = os.path.join(
                    path,
                    file.name
                )

                with open(file_path, "wb") as f:
                    f.write(file.getvalue())

            process_document(path)

        st.success("Documents processed successfully!")

        st.rerun()


if (
    st.session_state.document_uploaded
    and st.session_state.agent
):

    for message in st.session_state.messages:

        role = message.get("role")
        content = message.get("content")

        st.chat_message(role).markdown(content)

    query = st.chat_input(
        "Ask something about your documents..."
    )

    if query:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": query
            }
        )

        st.chat_message("user").markdown(query)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                response = st.session_state.agent.invoke(
                    {
                        "messages": [
                            {
                                "role": "user",
                                "content": query
                            }
                        ]
                    },
                    {
                        "configurable": {
                            "thread_id": "1"
                        }
                    }
                )

                answer = response["messages"][-1].content

                st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )