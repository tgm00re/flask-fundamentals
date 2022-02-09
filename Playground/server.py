from ast import Num
from turtle import color
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html", num=3, color="teal")

@app.route('/<int:num>')
def num(num):
    return render_template("index.html", num=num, color="teal")

@app.route('/<int:num>/<string:color>')
def full(num, color):
    return render_template("index.html", num=num, color=color)





if __name__ == "__main__": #ensure file is being run directly and not from a different module
    app.run(debug=True)