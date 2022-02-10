from flask import Flask, redirect, session,request, render_template
import random

app = Flask(__name__)
app.secret_key ="abcd1234"

@app.route('/')
def root():
    if('coins' not in session):
        session['coins'] = 0
    if('locations' not in session):
        session['locations'] = []
    if('coins_earned' not in session):
        session['coins_earned'] = []
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    print("Processing")
    request_type = request.form['process_type']
    location_list = session['locations']
    coins_earned_list = session['coins_earned']
    if(request_type == "farm"):
        randNum = random.randint(5,10)
        session['coins'] += randNum
        coins_earned_list.append(randNum)
        location_list.append('farm')
    elif(request_type == "cave"):
        randNum = random.randint(10,20)
        session['coins'] += randNum
        coins_earned_list.append(randNum)
        location_list.append('cave')
    elif(request_type == "house"):
        randNum = random.randint(2,5)
        session['coins'] += randNum
        coins_earned_list.append(randNum)
        location_list.append('house')
    elif(request_type == "casino"):
        if(session['coins'] >= 50):
            randNum = random.randint(0,1)
            if(randNum == 0):
                session['coins'] += 50
                coins_earned_list.append(50)
            elif(randNum == 1):
                session['coins'] -= 50
                coins_earned_list.append(-50)
            location_list.append('casino')
    session['locations'] = location_list
    session['coins_earned'] = coins_earned_list
    print(session['coins_earned'])
    return redirect('/')

@app.route('/hard_reset')
def hard_reset():
    session.clear()
    return redirect('/')



if __name__ == "__main__": #ensure file is being run directly and not from a different module
    app.run(debug=True)
