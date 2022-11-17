import sqlite3

db = sqlite3.connect('shuler.db', detect_types=sqlite3.PARSE_DECLTYPES)

db.execute("DELETE from stats")
db.commit()

db.execute("UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'stats'")
db.commit()
