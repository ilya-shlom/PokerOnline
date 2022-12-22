import sqlite3

db = sqlite3.connect('shuler.db', detect_types=sqlite3.PARSE_DECLTYPES)
db.row_factory = sqlite3.Row

db.execute("DELETE from users")
db.commit()

db.execute("UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'users'")
db.commit()

# user = db.execute('SELECT * FROM users WHERE game_key = ?', (game_key,)).fetchone()['username']
# id = db.execute('SELECT * FROM users WHERE game_key = ?', (game_key,)).fetchone()['id']
#
# db.execute("INSERT INTO stats (player_id, res, using_cheats) VALUES (?, ?, ?)",
#                                  (id, res_game, 'n'))
# db.commit()



