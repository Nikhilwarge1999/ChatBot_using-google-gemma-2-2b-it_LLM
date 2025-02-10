from model_load import get_response

def chatbot():
    print("Welcome to the Hugging Face Chatbot! Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = get_response(user_input)
        print(f"AI: {response}")

if __name__ == "__main__":
    chatbot()
    