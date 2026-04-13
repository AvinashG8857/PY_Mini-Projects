responses = {
    "hello":"Hi! there!",
    "how":"I'm doing fine, thanks!",
    "name":"I'm simple Chatbot.",
    "bye":"GoodBye!"
}

def chatbot():
    print("Chatbot: Start chatting! Type 'q' to quit")
    while True:
        user_input = input("You :").lower()
        if user_input == "q":
            print("Chatbot: Bye")
            break
        response = responses.get(user_input, "I dont Understand that.")
        print("Chatbot: ", response)
        
chatbot()