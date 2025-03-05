import streamlit as st
from model_load import get_response

st.markdown(
    """
    <head>
        <link rel="icon" href="https://raw.githubusercontent.com/Nikhilwarge1999/ChatBot_using-google-gemma-2-2b-it_LLM/main/Untitled%20design%20(2).png" type="image/png">
        <meta name="apple-mobile-web-app-title" content="MH_Bot">
    </head>
    """,
    unsafe_allow_html=True
)


# Page Configuration
st.set_page_config(page_title="AI Mental Helth Bot", page_icon="🧠", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #141414;
        }
        .main {
            background: url("https://images.unsplash.com/photo-1521747116042-5a810fda9664") no-repeat center center fixed;
            background-size: cover;
            color: black;
        }
        .chat-container {
            max-width: 600px;
            margin: auto;
            padding: 20px;
        }
        .user-message {
            text-align: right;
            background-color: #89d9f2;
            padding: 12px;
            border-radius: 20px;
            max-width: 70%;
            margin-left: auto;
            color: black;
        }
        .bot-message {
            text-align: left;
            background-color: #232323;
            padding: 12px;
            border-radius: 20px;
            max-width: 70%;
            color: white;
        }
        .message-container {
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }
        .avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            margin-right: 10px;
        }
        .header {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Chatbot UI
st.markdown('<div class="header">🤖 AI Chat Assistant</div>', unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! 😊 I'm your AI assistant. How can I help you today?"}
    ]

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="message-container"><div class="user-message">{msg["content"]}</div></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'''
            <div class="message-container">
                <img src="https://cdn-icons-png.flaticon.com/512/4712/4712031.png" class="avatar">
                <div class="bot-message">{msg["content"]}</div>
            </div>
        ''', unsafe_allow_html=True)

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Append user input
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.markdown(f'<div class="message-container"><div class="user-message">{user_input}</div></div>', unsafe_allow_html=True)

    # Get AI response
    with st.chat_message("assistant"):
        try:
            response = get_response(user_input)
        except Exception as e:
            response = "⚠️ I'm having trouble responding. Please try again later."

    # Append bot response
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.markdown(f'''
        <div class="message-container">
            <img src="https://cdn-icons-png.flaticon.com/512/4712/4712031.png" class="avatar">
            <div class="bot-message">{response}</div>
        </div>
    ''', unsafe_allow_html=True)
