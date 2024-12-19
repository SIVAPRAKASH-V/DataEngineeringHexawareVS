import re

# Knowledge base for FAQs and troubleshooting
knowledge_base = {
    "greetings": ["hello", "hi", "hey", "good morning", "good evening"],
    "faq": {
        "return policy": "Our return policy allows you to return items within 30 days of purchase.",
        "shipping time": "Shipping typically takes 3-5 business days.",
        "store hours": "We are open from 9 AM to 9 PM, Monday through Saturday.",
    },
    "troubleshooting": {
        "login issue": "If you're having trouble logging in, try resetting your password using the 'Forgot Password' link.",
        "payment issue": "If your payment is not going through, check your card details or try a different payment method.",
        "slow website": "Clear your browser cache or try accessing the website using a different browser.",
    },
}

def greet_user():
    print("Chatbot: Hello! Welcome to our customer service. How can I assist you today?")

def process_user_input(user_input):
    # Normalize input
    user_input = user_input.lower()

    # Check for greetings
    if any(greet in user_input for greet in knowledge_base["greetings"]):
        return "Hi there! How can I help you today?"

    # Check for FAQs
    for key, response in knowledge_base["faq"].items():
        if re.search(key, user_input):
            return response

    # Check for troubleshooting
    for key, response in knowledge_base["troubleshooting"].items():
        if re.search(key, user_input):
            return response

    # Default response
    return "I'm sorry, I didn't understand that. Can you please provide more details or rephrase your question?"

# Main chatbot loop
def chatbot():
    greet_user()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Thank you for reaching out! Have a great day!")
            break
        response = process_user_input(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
