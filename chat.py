from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

# Load environment variables from .env file
load_dotenv()

# Streamlit Page Setup
st.set_page_config(
    page_title="🤖🧠🇦🇮👾 Generative AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖🧠🇦🇮👾 Generative AI Chatbot")

# Initialize the Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show the chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Initialize LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.0,
)

# User input
user_prompt = st.chat_input("Ask Chatbot anything...")

if user_prompt:
    # Display user message
    st.chat_message("user").markdown(user_prompt)

    # Save user message
    st.session_state.chat_history.append(
        {"role": "user", "content": user_prompt}
    )

    # Get response from LLM
    response = llm.invoke(
        input=[
            {"role": "system", "content": "You are a helpful assistant."},
            *st.session_state.chat_history,
        ]
    )

    assistant_response = response.content

    # Save assistant response
    st.session_state.chat_history.append(
        {"role": "assistant", "content": assistant_response}
    )

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)