
# HealthChatBot

**HealthChatBot** is a conversational AI chatbot designed to provide personalized fitness guidance. It includes features such as BMI calculation, tailored workout and diet plans, and interactive conversational capabilities. Built with Flask and TensorFlow, it integrates with OpenAI's GPT API for handling complex queries.

---

## Features
- **Dynamic Intent Classification**: Classifies user queries into predefined intents using a bag-of-words model and a neural network.
- **Personalized Recommendations**: Generates BMI-based workout and diet plans.
- **GPT Fallback**: Uses OpenAI's GPT API for handling complex or untrained queries.
- **Session Management**: Tracks user input context during conversations for seamless interactions.
- **Web Interface**: Responsive HTML/CSS interface for user-friendly interactions.
- **Ngrok Integration**: Allows public access to the chatbot during development and testing.

---

## Project Structure

### Key Files
- **`intents.json`**: Annotated dataset for training the neural network. Contains user patterns, responses, and intent tags.
- **`training.py`**: Script to preprocess data, train the neural network model, and save it for inference.
- **`app.py`**: Main Flask application to handle user inputs, classify intents, and generate responses.
- **`requirements.txt`**: List of Python dependencies required for the project.
- **`templates/`**: Contains HTML templates for the chatbot interface.
- **`static/`**: Contains CSS and JavaScript files for styling and interactivity.

---

## Installation

### Clone the Repository
```bash
git clone https://github.com/FredYuL/HealthChatBot.git
cd HealthChatBot
```

### Install Dependencies
Use pip to install the required packages:
```bash
pip install -r requirements.txt
```

**Note**: Ensure compatibility between the versions of TensorFlow, NumPy, and Python. For best results, use Python 3.7 or 3.8 with the matching versions listed in `requirements.txt`.

---

## Optional: Retrain the Model
If you want to retrain the model with updated data in `intents.json`:
```bash
python training.py
```

---

## Run the Chatbot

### Launch the Server
Start the chatbot server:
```bash
python app.py
```

### Testing
Run the built testing file by 
```
python test.py
```

## Possible Issues and Solutions
- **Installation Problems**: Ensure all package versions listed in `requirements.txt` are compatible. Using Python 3.7 or 3.8 is recommended.
- **Environment Errors**: Create a virtual environment to manage dependencies and avoid conflicts:
  ```bash
  python -m venv venv
  source venv/bin/activate   # On Windows: venv\Scripts\activate
  ```
- **Retraining Issues**: Ensure `intents.json` is properly structured and matches the input format expected by `training.py`.

---


