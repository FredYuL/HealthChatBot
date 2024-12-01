from flask import session, request, render_template, jsonify
import openai
import os
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
import random
from tensorflow.keras.models import load_model
from flask import Flask
from flask_cors import CORS
from functions import calculate_bmi, create_workout_plan_with_BMI, create_diet_plan_with_BMI, create_workout_plan, create_diet_plan

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "my-secret-key"
cors = CORS(app)

# Download required NLTK data
nltk.download('punkt_tab')
nltk.download('wordnet')

# Initialize lemmatizer and load pre-trained assets
lemmatizer = WordNetLemmatizer()
intents = json.loads(open("intents.json").read())
words = pickle.load(open("words.pkl", 'rb'))
classes = pickle.load(open("classes.pkl", 'rb'))
model = load_model("chatbot_model.h5")

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Ensure the API key is set as an environment variable

# Helper Functions
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.5
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)

    # Ensure there's at least one result that crosses the threshold
    if results:
        return [{'intent': classes[r[0]], 'probability': str(r[1])} for r in results]
    else:
        return None


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

def chatgpt_response(prompt):
    import openai
    try:
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



# Routes
@app.route("/")
def index():
    session["bmi_category"] = " "
    session["order"] = ""
    return render_template('chat.html')

@app.route("/get", methods=["POST"])
def chat():
    print("Inside Chat function")
    msg = request.form["msg"]
    input = msg.lower()

    # Check for custom intents like BMI first
    if "," in input:  # User provides weight, height, and age
        try:
            input_values = input.split(',')
            weight, height, age = map(float, input_values)
            result = calculate_bmi(weight, height, age)
            session["bmi_category"] = result[1]
            return result[0]
        except ValueError:
            return "Please provide valid inputs in the format: weight,height,age."

    # Handle fitness level inputs
    if input in ["beginner", "intermediate", "advanced"]:
        if session["order"] == 'personalized_workout_plan':
            return create_workout_plan_with_BMI(input, session["bmi_category"])
        elif session["order"] == 'personalized_diet_plan':
            return create_diet_plan_with_BMI(input, session["bmi_category"])
        else:
            return create_workout_plan(input)

    # Predict intent using the trained model
    try:
        intents_list = predict_class(input)
        if intents_list:  # Valid intent found
            response = get_response(intents_list, intents)
            print(f"Matched Intent: {intents_list[0]['intent']}")
            return response
        else:  # Fallback to ChatGPT
            print("No matching intents found, falling back to ChatGPT.")
            return chatgpt_response(msg)
    except Exception as e:
        print(f"Error during intent prediction: {e}")
        return "Sorry, I couldn't understand your message."


if __name__ == '__main__':
    app.run()
