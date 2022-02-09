from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:word>')
def say(word):
    return f"Hi {word}".title()

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    return word*num

@app.errorhandler(404)
def errorMessage(e):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)