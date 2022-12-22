import random
from math import cos, pi, sin
import sqlite3

db = sqlite3.connect('shuler.db', detect_types=sqlite3.PARSE_DECLTYPES)
db.row_factory = sqlite3.Row

def rand_id():
    return random.getrandbits(64)


def get_info(game_key):
    user = db.execute('SELECT * FROM users WHERE game_key = ?', (game_key,)).fetchone()['username']
    id = db.execute('SELECT * FROM users WHERE game_key = ?', (game_key,)).fetchone()['id']
    return id, user


def put_info(game_key, res_game):
    inf = get_info(game_key)
    db.execute("INSERT INTO stats (player_id, res, using_cheats) VALUES (?, ?, ?)",
               (inf[0], res_game, 'n'))
    db.commit()


def rand_circle_pos(r=3000):
    angle = random.uniform(0, 2 * pi)
    return r * sin(angle), r * cos(angle)


def debug_start():
    import os
    from kivy.config import Config

    x = os.environ.get('x', 50)
    y = os.environ.get('y', 50)

    Config.set('graphics', 'position', 'custom')
    Config.set('graphics', 'left', x)
    Config.set('graphics', 'top', y)
