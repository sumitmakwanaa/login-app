from flask import Flask, render_template, request, url_for
import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='',database='app')
cursor = conn.cursor()



app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/login_validation', methods=['POST'])
def login_validation():
    user = request.form.get('username')
    pass1 = request.form.get('password')

    cursor.execute("""SELECT * FROM register WHERE 'username' LIKE 'user' AND 'password' LIKE 'pass1'""")
    app = cursor.fetchall()
    print(app)
    return 'helloo'


if __name__ == '__main__':
    app.run(debug = True)