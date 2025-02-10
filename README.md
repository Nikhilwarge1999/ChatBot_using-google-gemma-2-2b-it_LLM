# **🧠 AI-Powered Health Chatbot**  

## **📌 Project Overview**  
This repository contains the code for an **AI-driven Mental Health Chatbot** that provides **empathetic and intelligent conversations** to users seeking emotional support. The chatbot leverages **Generative AI, Natural Language Processing (NLP), and the `google/gemma-2-2b-it` model** to deliver context-aware responses. It is built using **Streamlit** for an intuitive and visually appealing user experience.  

---  
## **🚀 Features**  
✔ **Conversational AI** – Provides human-like conversations for mental health support.  
✔ **Pretrained LLM Model (`google/gemma-2-2b-it`)** – Generates responses using Hugging Face Inference API.  
✔ **User-Friendly UI** – Built with **Streamlit** for a seamless and visually stunning interface.  
✔ **Conversation History** – Maintains chat history for a natural dialogue flow.  
✔ **Anonymous & Secure** – Ensures user privacy and **does not store sensitive data**.  
✔ **Institution Branding** – Displays project affiliation with **College of Engineering and Technology, Akola**.  

---  
## **📌 Tech Stack**  
🔹 **Frontend:** Streamlit (for chatbot UI)  
🔹 **Backend:** Hugging Face Inference API  
🔹 **Model:** `google/gemma-2-2b-it` (LLM for chatbot responses)  
🔹 **Programming Language:** Python  
🔹 **Deployment:** Streamlit Cloud  

---  
## **🛠 Installation & Setup**  
### **1️⃣ Clone the Repository**  
```bash  
git clone https://github.com/your-username/mental-health-chatbot.git  
cd mental-health-chatbot  
```  

### **2️⃣ Install Dependencies**  
Ensure you have Python installed, then install the required libraries:  
```bash  
pip install -r requirements.txt  
```  

### **3️⃣ Set Up API Keys**  
Create a `.env` file and add your **Hugging Face API key**:  
```plaintext  
HUGGINGFACE_API_KEY=hf_xxxxxxxxxxxxxxxxxxxxxxxx  
```  

### **4️⃣ Run the Chatbot**  
```bash  
streamlit run app.py  
```  

---  
## **📌 Project Structure**  
```
mental-health-chatbot/
│── app.py                 # Main Streamlit chatbot UI
│── model_load.py          # Loads and interacts with Hugging Face API
│── requirements.txt       # List of dependencies
│── .env                   # API key storage (ignored in Git)
│── README.md              # Project documentation
```  

---  
## **🧠 How It Works**  
1️⃣ User enters a query in the chatbot UI.  
2️⃣ The chatbot sends the query to Hugging Face’s **Inference API** using `google/gemma-2-2b-it`.  
3️⃣ AI generates a response and sends it back to the UI.  
4️⃣ The response is displayed in a **scrollable chat format**.  

---  
## **🎯 Future Enhancements**  
✅ **Voice-Based Interaction** for improved accessibility.  
✅ **Emotion Recognition** to personalize responses based on user sentiment.  
✅ **Hybrid AI-Therapist Model** for professional intervention when needed.  

---  
## **📜 License**  
This project is open-source under the **MIT License**. Feel free to use, modify, and contribute!  

---  
## **🙌 Contributors**  
👤 **Your Name** – Developer  
💬 Feel free to **open issues** or **submit pull requests**!  

🔗 **GitHub Repo:**    https://github.com/Nikhilwarge1999/ChatBot_using-google-gemma-2-2b-it_LLM

