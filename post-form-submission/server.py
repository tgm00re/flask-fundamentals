from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe" #In practice, this should be a random string of bytes. 

@app.route('/')
def root():
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    #Write data to the session 
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    #NEVER RENDER A TEMPLATE TO A POST REQUEST
    #INSTEAD WE REDIRECT THE USER TO OUR INDEX ROUTE 
    return redirect('/show')

@app.route('/show')
def show_user():
    print("Showing the user info from the form")
    return render_template("show.html", name_on_template=session['username'])

#SESSION DATA CAN BE ACCESSED DIRECTLY VIA JINJA OR PASSED IN AS A VARIABLE
#I.E:
# <h3>{{session['username']}}</h3>
#CHECK show.html FOR MORE 




if __name__ == "__main__": #ensure file is being run directly and not from a different module
    app.run(debug=True)