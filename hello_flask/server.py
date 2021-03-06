from os import name
from flask import Flask, render_template #import flask 
app = Flask(__name__) #create a new instance of the flask class called "app"

@app.route('/')  #The '@' decorator associates this route with the function immediately following
def hello_world():
    return render_template("index.html") #templates folder must be called 'templates' 

@app.route('/success')
def success():
    return "Success!"


@app.route('/hello/<string:name>/<int:num>') #path variables always default to strings. We COULD type cast to what we need OR we can use built-in flask converters (i.e: <string: varName>)
def hello(name,num):
    return render_template("hello.html", name=name, num=num)

@app.route('/lists')
def render_lists():
    #We'll get data from databases soon, but for now we are hard-coding data
    student_info = [
       {'name' : 'Michael', 'age' : 35},
       {'name' : 'John', 'age' : 30 },
       {'name' : 'Mark', 'age' : 25},
       {'name' : 'KB', 'age' : 27}
    ]

    return render_template("lists.html", random_numbers =[3,1,5], students = student_info)


if __name__ == "__main__": #ensure file is being run directly and not from a different module
    app.run(debug=True)

