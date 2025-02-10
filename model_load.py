import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("HF_API_KEY")

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
