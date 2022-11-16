from flask import Flask, render_template, request, flash
from flask_restful import Api, Resource, reqparse
from db import get_db

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/gamepage')
def gamepage():
    return render_template("gamepage.html")


@app.route('/stats')
def stats():
    return render_template("stats.html")


@app.route('/settings')
def settings():
    return render_template("settings.html")


@app.route('/signup', methods=('GET', 'POST'))
def signup():
    return render_template("signup.html")


@app.route('/submit_acc', methods=('GET', 'POST'))
def submit_acc():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db()
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        if error is None:
            try:
                db.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                           (username, password))
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return render_template("index.html")
        flash(error)
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)

