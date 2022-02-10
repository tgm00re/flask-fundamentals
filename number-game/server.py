from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)

app.secret_key = "abcd1234"


@app.route('/')
def root():
    if('firstNames' not in session):
        session['firstNames'] = []
        session['scores'] = []
    if('guesses' not in session): #Start game!
        session['guesses'] = 0
        session['number'] = random.randint(1,100)
        session['helper'] = 0
        print(session['number'])
        session['guessed'] = False
    else:
        print(session['guessed'])
    return render_template("index.html")

@app.route('/take_guess', methods=['POST'])
def take_guess():
    session['guesses'] += 1
    if(int(request.form['guess']) == int(session['number'])):
        session['guessed'] = True
    elif(int(request.form['guess']) > int(session['number'])):
        session['helper'] = 1
    else:
        session['helper'] = -1
    return redirect('/')

@app.route('/take_name', methods=['POST'])
def take_name():
    first_list = session['firstNames']
    first_list.append(request.form['name'])
    score_list = session['scores']
    score_list.append(session['guesses'])
    # score_list = session['scores'].append(session['guesses'])
    session['firstNames'] = first_list
    session['scores'] = score_list
    return redirect('/leaderboard')

@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html", first_list=session['firstNames'], score_list=session['scores'])

@app.route('/reset_game')
def reset_game():
    session.pop('guesses')
    session.pop('number')
    session.pop('guessed')
    return redirect('/')

@app.route('/hard_reset')
def hard_reset():
    session.clear()
    return redirect('/')





if(__name__ == "__main__"):
    app.run(debug=True)