🌿 ***AI-Powered Health Chatbot*** 🤖 \n
🚀 A Generative AI-based chatbot for mental health support, built with google/gemma-2-2b-it, Hugging Face API, and Streamlit.

🔹 Project Overview
This AI-powered chatbot provides empathetic, anonymous, and interactive conversations for individuals seeking mental health support. It uses Generative AI and NLP to offer guidance, self-care tips, and emotional assistance.

🛠 Tech Stack
LLM Model: google/gemma-2-2b-it (Hugging Face API)
Frameworks: Transformers, LangChain, Streamlit
Backend: Python, huggingface_hub API
Deployment: Streamlit Cloud
📌 Features
✔ Conversational AI trained for mental health discussions
✔ Anonymous & Secure interaction with no user data storage
✔ Real-time Response using Hugging Face Inference API
✔ User-Friendly UI with an elegant, responsive design
✔ Conversation History for a natural chat flow
✔ Fine-Tuned Model with ramachaitanya22/mental_health_and_fitness_data

🚀 Installation & Usage
1️⃣ Clone the Repository

git clone https://github.com/your-username/mental-health-chatbot.git
cd mental-health-chatbot
2️⃣ Install Dependencies

pip install -r requirements.txt
3️⃣ Set Up API Keys
Create a .env file and add your Hugging Face API key:
env

HF_API_KEY=your_huggingface_api_key
4️⃣ Run the Chatbot

streamlit run app.py
📂 Project Structure

📂 health-chatbot
│── 📄 app.py                 # Streamlit UI for chatbot
│── 📄 model_load.py          # Loads the LLM model via API
│── 📄 requirements.txt       # Dependencies
│── 📄 .env                   # API key storage
│── 📂 assets                 # Images and media for UI
🚀 Deployment
Hosted on Streamlit Cloud for public access.
📜 License

This project is open-source and available under the MIT License.
