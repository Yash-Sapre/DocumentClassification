from flask import Flask,request

app = Flask(__name__)

@app.route("/",methods = ['GET','POST'])
def hello_world():
    if request.method == "POST":
        print(request.form['document'])
        print(request.form['category'])

        return '{"name":"Yash","surname":"Sapre"}'
    return "This is GET request No Use"