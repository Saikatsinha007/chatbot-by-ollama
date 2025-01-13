import streamlit as st
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import tiktoken
import requests
import faiss
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain.prompts import ChatPromptTemplate

# File uploader for PDF files
uploaded_files = st.file_uploader("Upload PDF Files", type="pdf", accept_multiple_files=True)

# Initialize the vector store and embedding model
embeddings = OllamaEmbeddings(model='nomic-embed-text', base_url="http://localhost:11434")

def load_documents(files):
    docs = []
    for file in files:
        loader = PyMuPDFLoader(file)
        docs.extend(loader.load())
    return docs

# Process uploaded PDFs
if uploaded_files:
    docs = load_documents(uploaded_files)
    st.write(f"Loaded {len(docs)} pages from uploaded PDFs.")

    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(docs)
    st.write(f"Split documents into {len(chunks)} chunks.")

    # Embedding and storing the chunks in FAISS
    index = faiss.IndexFlatL2(embeddings.embed_query("test").shape[0])
    vector_store = FAISS(
        embedding_function=embeddings,
        index=index,
        docstore=InMemoryDocstore(),
        index_to_docstore_id={}
    )
    vector_store.add_documents(documents=chunks)
    st.write("Documents indexed successfully.")

    # User input for question
    question = st.text_input("Enter your question:")

    if question:
        # Search for relevant documents
        docs = vector_store.search(query=question, search_type='similarity')

        # Prepare the context for question-answering
        context = "\n\n".join([doc.page_content for doc in docs])

        # Prepare the prompt template
        prompt = """
            You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question.
            If you don't know the answer, just say that you don't know.
            Answer in bullet points. Make sure your answer is relevant to the question and it is answered from the context only.
            Question: {question} 
            Context: {context} 
            Answer:
        """
        prompt_template = ChatPromptTemplate.from_template(prompt)

        # Format prompt with context and question
        formatted_prompt = prompt_template.format(question=question, context=context)

        # Send the formatted prompt to the Ollama API (replace with actual API URL and model)
        response = requests.post(
            "http://localhost:11434/v1/engines/llama3.2:1b/completions", 
            headers={"Content-Type": "application/json"},
            json={"prompt": formatted_prompt, "max_tokens": 500}
        )

        # Display the answer
        if response.status_code == 200:
            output = response.json()['choices'][0]['text']
            st.write("Answer:")
            st.write(output)
        else:
            st.write("Error querying the model.")
