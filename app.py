from flask import Flask, render_template, request, flash, session, redirect, url_for, send_file
from flask_restful import Api, Resource, reqparse
import subprocess
import db
import os
import logging
import random

level = logging.DEBUG
logger = logging.getLogger()
logger.setLevel(level)
for handler in logger.handlers:
    handler.setLevel(level)
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
        user = "Вход не выполнен"
    return render_template("index.html", out=str(user), state=log_state)


@app.route('/gamepage')
def gamepage():
    log_state = 0
    user_id = session.get('user_id', default=None)
    database = db.get_db()
    if user_id:
        log_state = 1
        user = user_id
        print(user)
        user = database.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()['username']
        game_key = database.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()['game_key']
        return render_template("gamepage.html", out=str(game_key), state=log_state)

    # здесь тоже не выводится
    else:
        user = "Not logged in"
        return render_template("login.html")
    # и здесь



@app.route('/download_win')
def download_win():
    path = "client.py"
    return send_file(path, as_attachment=True)


@app.route('/download_macos')
def download_macos():
    path = "client.py"
    return send_file(path, as_attachment=True)

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
    return render_template("stats.html", out_user=str(user), out_g=str(game), out_w=str(win), out_l=str(lose),
                           out_c=str(cheat), state=log_state)


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
                game_key = random.getrandbits(32)
                database.execute("INSERT INTO users (username, password, game_key) VALUES (?, ?, ?)",
                                 (username, password, game_key))
                database.commit()
                session.clear()
                session['user_id'] = database.execute('SELECT * FROM users WHERE username = ?',
                                                      (username,)).fetchone()['id']
            except database.IntegrityError:
                error = f"Пользователь {username} уже существует"
            else:
                return render_template("index.html", out=f"Добро пожаловать, {username}!")
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
            error = 'Неверный логин'
        elif user['password'] != password:
            error = 'Неверный пароль'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return render_template("index.html", out=f"С возвращением, {username}!")

        flash(error)

    return render_template("login.html", error=error)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.secret_key = os.urandom(30).hex() # Генерация секретного ключа для сессии пользователя
    app.run(debug=True, host='0.0.0.0')
