from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "1234abcd"


@app.route('/')
def root():
    if 'count' in session:
        session['count'] += 1
        if 'count_total' in session:
            session['count_total'] += 1
            print(session['count_total'])
        else:
            session['count_total'] = 1
    else:
        session['count'] = 1
    
    return render_template("index.html")

@app.route('/destroy_session')
def destroySession():
    session.clear() #clears all keys in session, recall session is similar to a dictionary
    return redirect('/')
    #session.pop('key_name') clears a specific key in session

@app.route('/add_two')
def addTwo():
    session['count'] += 1
    return redirect('/')

@app.route('/add_custom', methods=['POST'])
def add_custom():
    session['count'] += int(request.form['number']) - 1
    return redirect('/')

if __name__ == "__main__": #ensure file is being run directly and not from a different module
    app.run(debug=True)