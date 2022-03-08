
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import os
from nltk.tokenize import RegexpTokenizer
import pickle

def make_model(file_name,text,categories):
    model = MultinomialNB()
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(text)
    train_x = pd.DataFrame(X.toarray())
    train_y = pd.DataFrame(categories)
    model.fit(train_x,train_y.values.flatten())
    obj_lst = [model,vectorizer]
    with open(file_name,'ab') as model_file:
        pickle.dump(obj_lst,model_file)

def predict_text(file_name,text):
    with open(file_name,'rb') as model_file:
        obj_lst = pickle.load(model_file)
    
    model = obj_lst[0]
    vectorizer = obj_lst[1]
    test_x = vectorizer.transform([text])
    # test_x = pd.DataFrame(X.toarray())
    prediction = model.predict(test_x)
    return prediction[0]




