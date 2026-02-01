import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string


nltk.download('punkt')
nltk.download('stopwords')

stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there! How can I assist you?",
    "name": "I am an AI Chatbot built using NLP.",
    "python": "Python is a popular programming language for AI and data science.",
    "time": "I cannot access real-time clock, but I am always here to help!",
    "bye": "Goodbye! Have a nice day.",
    "help": "You can ask me about Python, AI, or general greetings."
}

def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [t for t in tokens if t not in string.punctuation]
    tokens = [t for t in tokens if t not in stop_words]
    stems = [stemmer.stem(t) for t in tokens]
    return stems

def get_response(user_input):
    processed = preprocess(user_input)

    for word in processed:
        if word in responses:
            return responses[word]

    return "Sorry, I didn't understand that. Can you rephrase?"


print("AI Chatbot with NLP (type 'bye' to exit)")
print("--------------------------------------")

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Bot: Goodbye! 👋")
        break

    bot_reply = get_response(user_input)
    print("Bot:", bot_reply)
