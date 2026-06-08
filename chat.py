def chatbot():
    print("Hello! I'm a simple chatbot.Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif 'hello' in user_input:
            print(f"Chatbot: You said '{user_input}'. That's interesting!")
        elif 'how are you' in user_input:
            print("Chatbot: I'm just a program, but I'm doing great! Thanks for asking.")
        elif 'what is your name' in user_input:
            print("Chatbot: I'm a simple chatbot created for demonstration purposes.")
        elif 'help' in user_input:
            print("Chatbot: I can help you with basic conversations. Just say hello or ask for help!")
        else:
            print(f"Chatbot: I'm not sure how to respond to '{user_input}', but I'm learning!")
chatbot()