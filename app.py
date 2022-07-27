from flask import Flask, render_template
from datetime import datetime

app = Flask("Hello!")

posts = [
    {
        "title": "o meu primeiro Post",
        "body": "Aqui é o texto do Post",
        "author": "Granato",
        "created": datetime(2022,7,25)
    },
    {
        "title": "o meu segundo Post",
        "body": "Aqui é o texto do Post",
        "author": "Feulo",
        "created": datetime(2022,7,26)
    },
]

@app.route("/") 
def index(): 
    return render_template("index.html", posts=posts)

@app.route( '/login')  
def login():
    return render_template("login.html")