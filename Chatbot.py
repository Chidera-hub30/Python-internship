def get_bot_response(user_input):


    clean_input = user_input.strip().lower()

    if "hello" in clean_input or "hi" in clean_input:
        return "Hi!"
    elif "how are you" in clean_input:
        return "I'm fine, thanks!"
    elif "bye" in clean_input or "goodbye" in clean_input:
        return "Goodbye!" 
    elif "tell me about yourself" in clean_input:
        return "First of all I am a python chatbot made by Geoffrey Chidera Anselm is that okay"
    else:
        return "I'm sorry, I don't understand that."


def start_chatbot():

    print("Chatbot: Hello! Type 'bye' to exit the chat.")

    while True:
        
        user_input = input("You: ")


        bot_response = get_bot_response(user_input)


        print(f"Chatbot: {bot_response}")


        if "bye" in user_input.lower() or "goodbye" in user_input.lower():
            break



start_chatbot()