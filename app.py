from flask import Flask, render_template, request, flash, session, redirect, url_for, blueprints
from flask_restful import Api, Resource, reqparse
import db
import os

app = Flask(__name__)
api = Api(app)
db.init_app(app)


@app.route('/')
def index():
    log_state = 0
    database = db.get_db()
    user_id = session.get('user_id', default=None)
    if user_id:
        log_state = 1
        user = user_id
        print(user)
        user = database.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()['username']

    else:
        user = "Not logged in"
    return render_template("index.html", out=str(user), state=log_state)


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

        database = db.get_db()
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        if error is None:
            try:
                database.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                                 (username, password))
                database.commit()
                session.clear()
                session['user_id'] = database.execute('SELECT * FROM users WHERE username = ?',
                                                      (username,)).fetchone()['id']
                return render_template("index.html", out=f"Welcome to the game, {username}!")
            except database.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return render_template("index.html")
        flash(error)
    return render_template("signup.html", error=error)


@app.route('/signin', methods=('GET', 'POST'))
def signin():
    return render_template("login.html")


@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        database = db.get_db()
        error = None
        user = database.execute('SELECT * FROM users WHERE username = ?', (username, )).fetchone()

        if user is None:
            error = 'Incorrect Username'
        elif user['password'] != password:
            error = 'Incorrect Password'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return render_template("index.html", out=f"Welcome back, {username}!")

        flash(error)

    return render_template("login.html", error=error)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.secret_key = os.urandom(30).hex()
    app.run(debug=True)
