# devops
DevOps AI Training Model Example Repo - Supporting a CI/CD Tutorial

#Supervised training

fasttext supervised -input questions.train -output model_questions > qtraining.log

#Predict


fasttext predict model_questions.bin questions.valid