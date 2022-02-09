from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    #NEVER RENDER A TEMPLATE TO A POST REQUEST
    #INSTEAD WE REDIRECT THE USER TO OUR INDEX ROUTE 
    return redirect('/')




if __name__ == "__main__": #ensure file is being run directly and not from a different module
    app.run(debug=True)