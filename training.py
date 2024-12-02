# Import necessary libraries
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, LearningRateScheduler
import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer

# Download the WordNet corpus (if not already downloaded)
nltk.download('wordnet')

# Initialize the WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# Load intents from the JSON file
with open("intents.json") as file:
    intents = json.load(file)

# Initialize lists to store words, classes, and documents
words = []  # To store all unique words from patterns
classes = []  # To store all unique tags (categories)
documents = []  # To store tuples of (word list, tag)
ignore_letters = ['?', "!", ".", ","]  # Characters to ignore during tokenization

# Process each intent in the intents JSON file
for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        # Tokenize each pattern into words
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)  # Add the words to the words list
        # Add the word list and corresponding tag as a tuple to the documents list
        documents.append((word_list, intent["tag"]))
        # Add the tag to the classes list if it's not already present
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lemmatize and clean up the words list
words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in ignore_letters]
words = sorted(set(words))  # Sort the words and remove duplicates

# Sort the classes (tags) and remove duplicates
classes = sorted(set(classes))

# Save the words and classes lists to files for later use
pickle.dump(words, open("words.pkl", 'wb'))
pickle.dump(classes, open("classes.pkl", 'wb'))

# Prepare training data
training = []  # List to store training data
output_empty = [0] * len(classes)  # Initialize an empty output vector for each class

# Create the training data
for document in documents:
    bag = []  # Bag of words for the current pattern
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    bag = [1 if word in word_patterns else 0 for word in words]

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

# Shuffle the training data
random.shuffle(training)

# Convert the training data into numpy arrays
train_x = np.array([x[0] for x in training])  # Input data
train_y = np.array([x[1] for x in training])  # Output data

# Build the neural network model
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(64, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation="softmax"))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer=Adam(learning_rate=0.001), metrics=['accuracy'])

# Adjust callbacks
early_stop = EarlyStopping(monitor='accuracy', patience=20, restore_best_weights=True)

def lr_schedule(epoch, lr):
    if epoch < 100:  # Constant learning rate for first 100 epochs
        return 0.001
    return lr * 0.9  # Gradual decay after 100 epochs

lr_scheduler = LearningRateScheduler(lr_schedule)

# Train with updated settings
model.fit(
    train_x,
    train_y,
    epochs=1000,  # Increased epochs
    batch_size=10,
    verbose=1,
    callbacks=[early_stop, lr_scheduler]
)

# Save the trained model
model.save('chatbot_model.h5')
print("Model training complete and saved as 'chatbot_model.h5'")
