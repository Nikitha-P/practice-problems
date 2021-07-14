from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
    return "Hello, world"



@app.route('/<name>')
def index2(name):
    return '<h1>Hello {}!</h1>'.format(name)

