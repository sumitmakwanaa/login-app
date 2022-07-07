from flask import Flask, render_template, request, jsonify, session
import psycopg2
import psycopg2.extras
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
from datetime import timedelta

app = Flask(__name__)

app.config['SECRET_KEY'] = 'sumitmakwanaa21327280'

app.config['PERMENENT_SESSION_LIFETIME'] = timedelta(minutes = 10) 
CORS(app)

DB_HOST = 'localhost'
DB_NAME = 'mydatabase'
DB_USER = 'postgres'
DB_PASS = 'sumitmakwanaa21327280'

conn = psycopg2.connect(dbname = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/signup_form', methods=['POST'])
def signup_form():
    passhash = generate_password_hash('sumit')
    print(passhash)
    return passhash

@app.route('/login_validation', methods=['POST'])
def login_validation():
    _username = request.form['username']
    _password = request.form['password']
    print(_password)
    
    if _username and _password:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        sql = "SELECT * FROM register WHERE username = '%s'"
        sql_where = (_username)

        cursor.execute(sql,sql_where)
        row = cursor.fetchone()
        username = row['username']
        password = row['password']

        if row:
            if check_password_hash(password,_password):
                session['username'] = username
                cursor.close()
                return jsonify({'message':'You are loged in successfully'})
            else:
                resp = jsonify({'message':'Bad Request - Invalid Password'})
                resp.status_code = 400
                return resp

    else:
        resp = jsonify({'message': 'Bad Request - Invalid credendtials'})
        resp.status_code = 400
        return resp


if __name__ == '__main__':
    app.run(debug = True)