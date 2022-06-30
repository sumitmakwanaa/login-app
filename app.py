from colorama import Cursor
from flask import Flask, render_template, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'app'
mysql = MySQL(app)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/login_validation', methods=['POST'])
def login_validation():
    user1 = request.form.get('username1')
    pass1 = request.form.get('password1')
    return 'hello'

@app.route('/signup_form', methods=['POST'])
def signup_form():
    user2 = request.form.get('username2')
    pass2 = request.form.get('password2')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO register (username, password) VALUES (%s, %s)", (user2, pass2))
    mysql.connection.commit()
    cur.close() 
    return ("username is {} and password is {}".format(user2, pass2))

if __name__ == '__main__':
    app.run(debug = True)