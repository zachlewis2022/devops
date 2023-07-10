import fasttext

# Training data file path
train_data_path = 'train.txt'

# Model output file path
model_output_path = 'model.bin'

# Preprocess the training data
preprocessed_train_data = []
with open(train_data_path, 'r') as file:
    for line in file:
        words = line.strip().split()
        sentence = ' '.join(words[:-1])  # Use all words except the last one as the input sentence
        label = words[-1]  # The last word is treated as the label
        preprocessed_train_data.append(f'__label__{label} {sentence}')

# Save the preprocessed training data to a new file
preprocessed_train_data_path = 'preprocessed_train.txt'
with open(preprocessed_train_data_path, 'w') as file:
    file.write('\n'.join(preprocessed_train_data))

# Train the FastText model
model = fasttext.train_supervised(preprocessed_train_data_path)

# Save the trained model
model.save_model(model_output_path)

# Load the trained model
model = fasttext.load_model(model_output_path)

# Sentence to predict the next word
sentence = "I love to"

# Predict the next word
next_word = model.predict(sentence)[0][0][9:]  # Extract the predicted word without the '__label__' prefix

# Print the predicted next word
print("Predicted Next Word:", next_word)
