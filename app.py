from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/login_validation', methods=['POST'])
def login_validation():
    username = request.form.get('username')
    password = request.form.get('password')
    return "The email is {} and the password is {}".format(username, password)

if __name__ == '__main__':
    app.run(debug = True)