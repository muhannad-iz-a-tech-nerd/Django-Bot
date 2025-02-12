from django.conf import settings

class __Chat:
    def __init__(self):
        # Initialize your chatbot logic here
        self.name = "SampleBot"  # Example attribute, change as needed
        self.responses = {
            "hello": "Hi there! How can I assist you today?",
            "bye": "Goodbye! Have a nice day!",
        }

    def get_response(self, user_input):
        # Basic response logic based on user input
        user_input = user_input.lower()
        
        # Simple matching for responses
        if user_input in self.responses:
            return self.responses[user_input]
        
        return "I'm sorry, I didn't understand that. Can you try again?"

chat = __Chat()  # This creates the chatbot instance

def start_chatbot_engine():
    from .handler import initiate_chat  # Import a function to handle chat initialization
    
    if hasattr(settings, "CHATBOT_TEMPLATE"):
        chat_obj = initiate_chat(settings.CHATBOT_TEMPLATE)
    else:
        chat_obj = initiate_chat()
    
    # Dynamically assign all attributes from chat_obj to the `chat` instance
    for attribute in dir(chat_obj):
        if attribute[0] != "_":  # Avoid private attributes
            setattr(chat, attribute, getattr(chat_obj, attribute))
