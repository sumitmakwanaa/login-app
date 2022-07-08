from ast import Return
from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

from mysqlx import Session

app = Flask(__name__)
app.secret_key = "123"

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/index')
def index():
    return 'index'

@app.route('/signup_form', methods=['POST'])
def signup_form():
    if (request.method == 'POST'):
        if  request.form['username']!="" and request.form['password'] != "":
            username = request.form['username']
            password = request.form['password']
            conn = sqlite3.connect('mydatabase.db')
            c = conn.cursor()
            c.execute("INSERT INTO register VALUES('"+username+"','"+password+"')")
            msg = "Register successfully"
            print(msg)
            conn.commit()
            conn.close()
        else:
            msg = "Register failed"
            print(msg)
    return render_template('login.html')    
        
            
@app.route('/login_validation', methods=['POST'])
def login_validation():
    if (request.method == 'POST'):
        if  request.form['username']!="" and request.form['password'] != "":
            username = request.form['username']
            password = request.form['password']
            conn = sqlite3.connect('mydatabase.db')
            c = conn.cursor()
            c.execute("SELECT * FROM register WHERE users= '"+username+"' and passwords= '"+password+"'")
            i = c.fetchone()
            if i and username == i[0] and password == i[1]:
                session["Loged in"] = True
                session["username"] = username
                return redirect(url_for("index"))
            else:
                return redirect(url_for("signin"))

        else:
            return "Please enter valid username and password" 
            

if __name__ == '__main__':
    app.run(debug = True)