import streamlit as st
# from huggingface_hub import InferenceClient

# # Use Streamlit secrets for API key
# API_KEY = st.secrets["HF_API_KEY"]

# # Initialize Hugging Face client
# client = InferenceClient(model="google/gemma-2-2b-it", token=API_KEY)

# def get_response(user_input):
#     try:
#         response = client.text_generation(
#             prompt=user_input,
#             max_new_tokens=500,
#             temperature=0.7,
#             top_p=0.95
#         )
#         return response
#     except Exception as e:
#         return f"Error: {str(e)}"
import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = st.secrets["HF_API_KEY"]

# Initialize Hugging Face Inference Client
client = InferenceClient(api_key=API_KEY)

def get_response(user_input):
    """Fetches response from the Hugging Face model."""
    try:
        messages = [{"role": "user", "content": user_input}]

        completion = client.chat.completions.create(
            model="google/gemma-2-2b-it",
            messages=messages,
            max_tokens=500
        )

        return completion.choices[0].message["content"]
    
    except Exception as e:
        return f"Error: {str(e)}"

