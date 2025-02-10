
import streamlit as st
from model_load import get_response

st.markdown("""
    <style>
        .user-message {
            text-align: right;
            background-color: #dcf8c6;
            padding: 10px;
            border-radius: 10px;
            max-width: 50%;
            margin-left: auto;
        }
        .bot-message {
            text-align: left;
            background-color: #f1f0f0;
            padding: 10px;
            border-radius: 10px;
            max-width: 70%;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 Health Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-message">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-message">{msg["content"]}</div>', unsafe_allow_html=True)

# User input
user_input = st.chat_input("Ask me anything...")
if user_input:
    # Append user input
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.markdown(f'<div class="user-message">{user_input}</div>', unsafe_allow_html=True)
    
    # Get AI response
    response = get_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    st.markdown(f'<div class="bot-message">{response}</div>', unsafe_allow_html=True)
 
