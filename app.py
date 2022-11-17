from flask import Flask, render_template, request, flash, session, redirect, url_for
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


@app.route('/gamepage', methods=('GET', 'POST'))
def gamepage():
    log_state = 0
    user_id = session.get('user_id', default=None)
    database = db.get_db()
    if user_id:
        log_state = 1
        user = user_id
        print(user)
        user = database.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()['username']

        if request.method == 'POST':
            win = request.form.get("win", False)
            lose = request.form.get("lose", False)
            database = db.get_db()
            val = 'w' if win is not False else 'l'
            try:
                database.execute("INSERT INTO stats (player_id, res, using_cheats) VALUES (?, ?, ?)",
                                 (user_id, val, 'n'))
                database.commit()
            except database.IntegrityError:
                error = "some errors :_("
            else:
                # здесь нужно поправить, т.к. не выводится юзер
                return render_template("gamepage.html", out=str(user) + " win!")

    # здесь тоже не выводится
    else:
        user = "Not logged in"
    # и здесь
    return render_template("gamepage.html", out=str(user), state=log_state)


@app.route('/stats')
def stats():
    log_state = 0
    win = 0
    lose = 0
    cheat = 0
    game = 0
    user_id = session.get('user_id', default=None)
    database = db.get_db()
    if user_id:
        log_state = 1
        user = database.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()['username']
        res = database.execute("SELECT res, using_cheats FROM stats WHERE player_id = ?", (user_id,)).fetchall()
        game, count = len(res), len(res) - 1
        while count >= 0:
            win += 1 if res[count][0] == 'w' else 0
            lose += 1 if res[count][0] == 'l' else 0
            cheat += 1 if res[count][1] == 'y' else 0
            count -= 1



    else:
        user = "Not logged in"
    return render_template("stats.html", out_user=str(user), out_g=str(game), out_w=str(win), out_l=str(lose), out_c=str(cheat),
                           state=log_state)


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
            except database.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return render_template("index.html", out=f"Welcome to the game, {username}!")
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
