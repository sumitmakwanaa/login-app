from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3


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
            conn.commit()
            conn.close()
            return render_template('login.html') 
        else:
            msg = "Register failed"
            return render_template('signin.html', msg=msg)
       
        
            
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
                msg = "Login successfully"
                return render_template('index.html', msg = msg)
            else:
                msg = "Couldn't login'"
                return render_template('login.html', msg=msg)  

        else:
            return "Please enter valid username and password" 
            

if __name__ == '__main__':
    app.run(debug = True)