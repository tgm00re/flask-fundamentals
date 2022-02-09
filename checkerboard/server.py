from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("index.html", numOne=8, numTwo=8, colorOne="red", colorTwo="black")

@app.route('/<int:numOne>')
def single(numOne):
    return render_template("index.html", numOne=numOne, numTwo=8, colorOne="red", colorTwo="black")

@app.route('/<int:numOne>/<int:numTwo>')
def double(numOne, numTwo):
    return render_template("index.html", numOne=numOne, numTwo=numTwo, colorOne="red", colorTwo="black")

@app.route('/<int:numOne>/<int:numTwo>/<string:colorOne>')
def triple(numOne, numTwo, colorOne):
    return render_template("index.html", numOne=numOne, numTwo=numTwo, colorOne=colorOne, colorTwo="black")

@app.route('/<int:numOne>/<int:numTwo>/<string:colorOne>/<string:colorTwo>')
def all(numOne, numTwo, colorOne, colorTwo):
    return render_template("index.html", numOne=numOne, numTwo=numTwo, colorOne=colorOne, colorTwo=colorTwo)


if __name__ == "__main__": #ensure file is being run directly and not from a different module
    app.run(debug=True)