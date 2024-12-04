# Import necessary libraries
from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS
from pyngrok import ngrok
import random
import openai
import os
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

# Import custom functions for BMI, workout, and diet plans
from functions import (
    calculate_bmi,
    create_workout_plan_with_BMI,
    create_diet_plan_with_BMI,
    create_workout_plan,
    create_diet_plan
)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "my-secret-key"  # Secret key for session management
cors = CORS(app)  # Enable Cross-Origin Resource Sharing (CORS)

# Download required NLTK data
nltk.download('punkt_tab')
nltk.download('wordnet')

# Initialize lemmatizer for text preprocessing
lemmatizer = WordNetLemmatizer()

# Load intents, words, classes, and the trained chatbot model
intents = json.loads(open("intents.json").read())
words = pickle.load(open("words.pkl", 'rb'))
classes = pickle.load(open("classes.pkl", 'rb'))
model = load_model("chatbot_model.h5")

# Set OpenAI API Key
#openai.api_key = os.getenv("OPENAI_API_KEY")  # Ensure the API key is set as an environment variable

# Function to preprocess user input: tokenize and lemmatize
def clean_up_sentence(sentence):
    """
    Tokenizes and lemmatizes the input sentence.
    Args:
        sentence (str): The input sentence from the user.
    Returns:
        list: A list of lemmatized words.
    """
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


# Function to create a "bag of words" representation of the input sentence
def bag_of_words(sentence):
    """
    Converts a sentence into a bag-of-words representation.
    Args:
        sentence (str): The input sentence from the user.
    Returns:
        np.array: A binary array indicating the presence of words in the vocabulary.
    """
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    """
    Predicts the intent of the input sentence using the trained model.
    Args:
        sentence (str): The input sentence from the user.
    Returns:
        list: A list of intents with their probabilities.
    """
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.5  # Define the error threshold
    
    # Calculate error rate
    max_probability = max(res)  # Get the highest probability from the prediction
    error_rate = 1 - max_probability  # Error rate is 1 - highest probability
    print(f"Current Error Rate: {error_rate:.2f}")  # Print the error rate with two decimal places

    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)

    # Ensure there's at least one result that crosses the threshold
    if results:
        return [{'intent': classes[r[0]], 'probability': str(r[1])} for r in results]
    else:
        return None



# Function to get a response based on the predicted intent
def get_response(intents_list, intents_json):
    try:
        if not intents_list:
            print("No matching intents found, falling back to ChatGPT.")
            return None
        tag = intents_list[0]['intent']
        for intent in intents_json['intents']:
            if intent['tag'] == tag:
                return random.choice(intent['responses'])
    except IndexError:
        print("No intents matched, falling back to ChatGPT.")
        return None
    return None

# ChatGPT Response Function
def chatgpt_response(prompt):
    import openai
    try:
        # Set your OpenAI API key here
        # Replace API key with yours, this one has been disabled. 
        openai.api_key = "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"
        
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a fitness chatbot specializing in personalized advice."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error with ChatGPT API: {e}")
        return "Sorry, I'm having trouble connecting to the ChatGPT API right now."




# Route for the main page
@app.route("/")
def index():
    """
    Renders the main chat page and initializes session variables.
    """
    session["bmi_category"] = " "  # Initialize BMI category
    session["order"] = ""  # Initialize order type
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    """
    Handles user input, predicts intent, and generates appropriate responses.
    """
    print("Inside Chat function")
    msg = request.form["msg"]  # Get user input
    input = msg.lower()
    print(f"User input: {input}")

    try:
        # Predict intent
        ints = predict_class(input)
        print(f"Predicted intents: {ints}")

        # Check if any intents were predicted
        if not ints:  # No intents above the error threshold
            print("No intents matched the error threshold.")
            response = chatgpt_response(input)
            return response

        # Print the error threshold for debugging
        print(f"Error threshold: 0.25")

        # Access the top intent
        top_intent = ints[0]['intent']
        print(f"Top intent: {top_intent}")

        # Handle personalized workout or diet plan requests
        if top_intent in ['personalized_workout_plan', 'personalized_diet_plan']:
            session["order"] = top_intent
            print(f"Order updated: {session['order']}")

        # Handle BMI calculation if user provides weight, height, and age
        if "," in input:
            input_values = input.split(',')
            try:
                weight, height, age = map(float, input_values)
                result = calculate_bmi(weight, height, age)
                session["bmi_category"] = result[1]
                print(f"BMI category set: {session['bmi_category']}")
                return result[0]
            except ValueError:
                return "Please provide valid inputs in the format: weight,height,age."

        # Handle fitness level inputs
        if input in ["beginner", "intermediate", "advanced"]:
            print(f"User level: {input}")
            if session["order"] == 'personalized_workout_plan':
                response = create_workout_plan_with_BMI(input, session["bmi_category"])
            elif session["order"] == 'personalized_diet_plan':
                response = create_diet_plan_with_BMI(input, session["bmi_category"])
            else:
                response = create_workout_plan(input)
            return response

        # Get response from intents
        response = get_response(ints, intents)
        return response

    except Exception as e:
        print(f"Error in chat function: {e}")
        return "Sorry, I couldn't process your request."


# Main function to run the Flask app
if __name__ == "__main__":
    """
    Starts the Flask app and sets up ngrok for public access.
    """
    # Set your ngrok authtoken
    ngrok.set_auth_token("2pd5QL3xXyvLZzvVSZHKgpM1bJx_77rNNJXvDUmH89iYV4dsB")  # Replace with your actual token

    # Start ngrok and get the public URL
    public_url = ngrok.connect(5000)
    print(f"Public URL: {public_url}")

    # Run the Flask app
    app.run(port=5000)
