import fasttext

# Training data file path
train_data_path = 'train.txt'

# Model output file path
model_output_path = 'model.bin'

# Train the FastText model
model = fasttext.train_unsupervised(train_data_path)

# Save the trained model
model.save_model(model_output_path)

# Load the trained model
model = fasttext.load_model(model_output_path)

# Sentence to predict the next word
sentence = "I love to"

# Predict the next word
next_word = model.predict(sentence, k=1)[0][0]

# Print the predicted next word
print("Predicted Next Word:", next_word)
