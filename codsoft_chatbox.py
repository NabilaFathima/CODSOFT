def codsoft_chatbox():
    print("Hello!. How can I help you?")
    while True:
        user=input("You: ").lower()
        
        if "hello" in user or "hi" in user:
            print("Chatbot: Hello! How can I assist you?")
        elif "internship" in user or "internships" in user:
            print("Chatbot: Codsoft offers internships in App Development,Python,Java,Artificial Intelligence,and more.")
        elif "duration" in user:
            print("Chatbot: The internship duration is 4 weeks.")
        elif "certificate" in user:
            print("Chatbot: Yes, certificates are provided after successful completion.")
        elif "tasks" in user or "projects" in user:
            print("Chatbot: You will need to complete atleast 3 tasks for successful completion of the internship.")
        elif "offer letter" in user:
            print("Chatbot: The offer letter is provided after you internship applichation is accepted.")
        elif "bye" in user:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("I'm sorry,I don't understand that. Can you try asking something else?")
          
        codsoft_chatbox()
