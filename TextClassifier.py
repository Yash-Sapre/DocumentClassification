

from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import os
from nltk.tokenize import RegexpTokenizer


# num = int(input("Enter the number of documents for training :"))
# categories = []
# text = []

# for i in range(0,num):
#     category = input("Enter the category :")
#     with open('D:/Infytyq problems/train_text.txt','r',encoding='utf-8') as file:
#         input_text = file.read()
#         input_text.strip('/n')
#         input_text.lower()
#     text.append(input_text)
#     categories.append(category)

training_documents_path = "D:/train documents/"
text = []
categories = []
tokenizer = RegexpTokenizer(r"\w+")
for file_name in os.listdir(training_documents_path):
    file_lines = []
    with open(training_documents_path + file_name , 'r' , encoding= 'utf-8') as file:
        for line in file:
            
            file_lines.append(line.lower())
        category = file_lines.pop(0)
        categories.append(category[0:len(category ) - 1])
        file_text = ' '.join(file_lines)
        final_file_text = ' '.join(tokenizer.tokenize(file_text))
        text.append(final_file_text)
        
print(categories)
model = MultinomialNB()
vectorizer = TfidfVectorizer()
X = 0
def make_model(text,categories):
    global X
    global model
    global vectorizer
    X = vectorizer.fit_transform(text)
    train_x = pd.DataFrame(X.toarray())
    
    train_y = pd.DataFrame(categories)
    
    model.fit(train_x,train_y.values.flatten())

make_model(text,categories)

def predict_text(text):
    global X
    global model
    global vectorizer
    
    test_x = vectorizer.transform([text])
    # test_x = pd.DataFrame(X.toarray())
    prediction = model.predict(test_x)
    return prediction

# test_text = input("Enter the document address: ")
test_text = 'D:/test documents/test_text.txt'
with open(test_text,'r',encoding='utf-8') as file:
    input_text = file.read()
    input_text.strip('/n')
    input_text.lower()
print(predict_text(input_text))

