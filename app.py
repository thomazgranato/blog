from flask import Flask, render_template

app = Flask("Hello!")

@app.route("/") 
@app.route("/hello")
def hello(): 
    return "Hello World"

@app.route("/meucontato")
def meuContao():
    return render_template("index.html")