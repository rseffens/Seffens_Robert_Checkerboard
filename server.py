from random import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def board():
    return render_template("index.html", x = 4, y = 4, color2="red", color1="black")

@app.route("/<int:x>")
def board1(x):
    return render_template("index.html", x = x, y = 8, color2="red", color1="black")

@app.route("/<int:x>/<int:y>")
def board2(x,y):
    return render_template("index.html", x = x, y = y, color2="red", color1="black")

if __name__=="__main__":
    app.run(debug=True)
    