from flask import Flask, render_template, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/gamepage')
def gamepage():
    return render_template("gamepage.html")


@app.route('/signup', methods=('GET', 'POST'))
def signup():
    return render_template("signup.html")


@app.route('/submit_acc', methods=('GET', 'POST'))
def submit_acc():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        print(12)
        data = open("logins.txt", "w")
        data.write(f'{username}\n{password}')
    return "Вы успешно зарегистрировались!"


if __name__ == "__main__":
    app.run(debug=True)

