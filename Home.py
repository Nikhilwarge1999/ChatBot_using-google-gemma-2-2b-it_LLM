import streamlit as st
import base64

# ✅ Must be the first Streamlit command
st.set_page_config(page_title="Mental Health Assistant", layout="wide")

# Function to encode local image
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load your local background image (make sure the image exists)
bg_image = get_base64_of_bin_file("bsa.jpg")

# Inject background CSS
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg_image}");
        background-size: 100%;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    .center-button {{
        display: flex;
        justify-content: center;
        margin-top: 30px;
        margin-bottom: 50px;
    }}
    .card {{
        background-color: rgba(255, 255, 255, 0.85);
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    }}
    h1, h2, h4, p {{
        color: #000000;
    }}
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }
    [data-testid="stSidebarNav"] {
        display: none;
    }
    [data-testid="collapsedControl"] {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Welcome Text
st.markdown("""
    <h1 style='
        text-align: center;
        color: black;
        font-size: 3em;
        text-shadow: 1px 1px 2px #ffffff, 0 0 10px #ffffff, 0 0 20px #ffffff;
    '>
        🧠 Welcome to the Mental Health Assistant
    </h1>
""", unsafe_allow_html=True)


# Centered Start Button
st.markdown('<div class="center-button">', unsafe_allow_html=True)
if st.button("🟢 Start Chat"):
    st.switch_page("pages\\ui.py")
st.markdown('</div>', unsafe_allow_html=True)

# Divider and Team Section
st.markdown("---")
st.markdown("""
    <h2 style="color:white; font-weight: bold; text-align: center;">
        🤝 Meet the Team
    </h2>
""", unsafe_allow_html=True)


# Team Member Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
        <div class="card">
            <h4>Nikhil</h4>
            <p>AI Engineer</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="card">
            <h4>Punam</h4>
            <p>Research Assistant</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="card">
            <h4>Shruti</h4>
            <p>UI/UX Designer</p>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div class="card">
            <h4>Rahul</h4>
            <p>Backend Developer</p>
        </div>
    """, unsafe_allow_html=True)
