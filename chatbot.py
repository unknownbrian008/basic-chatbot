def start_chatbot():
    print("🤖 Chatbot: Hi! I'm a simple chatbot.")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a great day 😊")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("🤖 Chatbot: Hello there!")

        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm doing great! Thanks for asking!")

        elif "your name" in user_input:
            print("🤖 Chatbot: I'm a basic Python chatbot.")

        elif "help" in user_input:
            print("🤖 Chatbot: Try saying hello or asking how I am.")

        else:
            print("🤖 Chatbot: Sorry, I didn't understand that.")


if __name__ == "__main__":
    start_chatbot()
