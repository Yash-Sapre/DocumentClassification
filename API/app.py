from flask import Flask,request
import classifier
app = Flask(__name__)

@app.route("/create",methods = ['GET','POST'])
def create():
    if request.method == "POST":
        content = request.get_json(silent=True)
        print(content)
        print(type(content))
        for metafield in content:
            text = content[metafield]['documents']
            categories = content[metafield]['categories']
            classifier.make_model(text,categories,metafield)

        return '{"status":"ok"}'
    return "This is GET request No Use"

@app.route("/predict",methods=['GET','POST'])
def predict():
    if request.method == "POST":
        content = request.get_json
        for metafield in content:
            text = content[metafield]['document']
            prediction = classifier.predict_text(text,metafield)
        return prediction

    return "This is GET request No Use"