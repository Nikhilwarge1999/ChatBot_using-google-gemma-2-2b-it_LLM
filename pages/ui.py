import streamlit as st
import time
from model_load import get_response
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
# st.title("🧠 Mental Health Chatbot UI")

# Inject Custom CSS
st.markdown("""
    <style>
    .chat-container {
        height: 0vh;
        overflow-y: auto;
        padding-right: 10px;
        margin-bottom: 1rem;
    }
    .user-message {
        text-align: right;
        background-color: #b4f283;
        padding: 12px;
        border-radius: 15px;
        margin-bottom: 10px;
        max-width: 70%;
        width: fit-content;
        margin-left: auto;
        color: black;
    }
    .bot-message {
        text-align: left;
        background-color: #2f3030;
        color: white;
        width: fit-content;
        padding: 12px;
        border-radius: 15px;
        margin-bottom: 10px;
        max-width: 70%;
    }
    </style>
""", unsafe_allow_html=True)


# Split into Streamlit columns (30%-70%)
col1, col2 = st.columns([4, 6], gap="large")

# ---------------- LEFT PANEL (Fixed) ---------------- #
with col1:
    # st.subheader("Mental Health Chatbot")
    
    st.markdown("""
        <div style="height: 50vh; overflow: hidden; background-color: #f5f5f5;
                    border-radius: 10px; padding: 15px; border: 2px solid #ddd;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);">
            <ul>
                <li>🔐 Private & Anonymous</li>
                <li>💡 Mental health tips</li>
                <li>📘 Resource links</li>
                <li>🌍 Multi-Language Support</li>
                <li>🧘 Relaxation Exercises</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# ---------------- RIGHT PANEL (Chat UI) ---------------- #
with col2:
    st.markdown("### Meantal Health AI Bot 🤖")
    st.markdown('<div class="chat-container" id="chat-box">', unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! 😊 I'm your AI assistant. How can I help you today?"}
        ]

    for i, msg in enumerate(st.session_state.messages):
        if msg["role"] == "user":
            st.markdown(f'<div class="user-message">{msg["content"]}</div>', unsafe_allow_html=True)
        else:
            if i == len(st.session_state.messages) - 1 and "just_added" in msg:
                placeholder = st.empty()
                typed = ""
                for ch in msg["content"]:
                    typed += ch
                    placeholder.markdown(f'<div class="bot-message">{typed}</div>', unsafe_allow_html=True)
                    time.sleep(0.02)
            else:
                st.markdown(f'<div class="bot-message">{msg["content"]}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Auto-scroll to latest
    components.html("""
        <script>
        const chatBox = window.parent.document.querySelector("#chat-box");
        if (chatBox) {
            chatBox.scrollTop = chatBox.scrollHeight;
        }
        </script>
    """, height=0)

# Input box fixed at bottom of the window
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        placeholder = st.empty()
        for i in range(3):
            placeholder.markdown("🤖 Bot is typing" + "." * (i + 1))
            time.sleep(0.4)

    response = get_response(user_input)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response,
        "just_added": True
    })

    st.rerun()
