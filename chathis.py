import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate
from langchain_core.prompts import ChatPromptTemplate

# App title and description
st.title(":snowman: Saikat the intellectual")
st.markdown("""
Welcome to your very own interactive chat application, 
created with the intellectual **Saikat Sinha**!  
Don't stress, **"ho jayega vai tension mat le, ja chocolate leke aaa"**
""")

# Initialize the model
model = ChatOllama(model="llama3.2:1b", base_url="http://localhost:11434/")

# Define the system message
system_message = SystemMessagePromptTemplate.from_template(
    "You are a helpful AI Assistant. You work as a teacher for 5th-grade students. You explain things in short and brief."
)

# Initialize chat history if not already done
if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []

# Function to generate response
def generate_response(chat_history):
    chat_template = ChatPromptTemplate.from_messages(chat_history)
    chain = chat_template | model | StrOutputParser()
    response = chain.invoke({})
    return response

# Function to build chat history from session state
def get_history():
    chat_history = [system_message]
    for chat in st.session_state['chat_history']:
        prompt = HumanMessagePromptTemplate.from_template(chat['user'])
        chat_history.append(prompt)
        ai_message = AIMessagePromptTemplate.from_template(chat['assistant'])
        chat_history.append(ai_message)
    return chat_history

# Sidebar for user input
with st.sidebar:
    st.header(":speech_balloon: Chat Interface")
    with st.form("llm-form"):
        text = st.text_area("Ask a question:", placeholder="Type your question here...")
        submit = st.form_submit_button("Submit")
    if submit and text:
        with st.spinner("Answer generate hone mein time lagta hein, tension mat le, tu tab tak chocolate leke aa!"):
            prompt = HumanMessagePromptTemplate.from_template(text)
            chat_history = get_history()
            chat_history.append(prompt)
            response = generate_response(chat_history)
            st.session_state['chat_history'].append({'user': text, 'assistant': response})

# Main content area for chat history
st.write("## :page_with_curl: Conversation History")
if st.session_state['chat_history']:
    for chat in reversed(st.session_state['chat_history']):
        st.markdown(f"**:cold_sweat: Gandu**: {chat['user']}")
        st.markdown(f"**:snowman: Saikat**: {chat['assistant']}")
        st.markdown("---")
else:
    st.info("No conversations yet. Start by asking a question from the sidebar!")

# Footer
st.markdown("""
---
Answer generate hone mein time lagta hein, tension mat le, tu tab tak chocolate leke aa! :chocolate_bar:
""")
