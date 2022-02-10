from crypt import methods
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "abcd1234"

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/submit_form', methods=['POST'])
def submit_form():
    req = request.form
    session['email'] = req.get('email')
    session['password'] = req.get('password')
    session['address'] = req.get('address')
    session['second-address'] = req.get('second-address')
    session['city'] = req.get('city')
    session['state'] = req.get('state')
    session['zip'] = req.get('zip')
    session['newsletter'] = req.get('newsletter')
    session['exampleRadios'] = req.get('exampleRadios')
    return redirect('/display_information')

@app.route('/display_information')
def display_information():
    return render_template("display_information.html")




if __name__ == "__main__":
    app.run(debug=True)