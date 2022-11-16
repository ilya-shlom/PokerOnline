DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS stats;

CREATE TABLE  users
(
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(20) UNIQUE NOT NULL,
    password VARCHAR(20)        NOT NULL
);

CREATE TABLE stats
(
    player_id    INTEGER,
    game_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    res          VARCHAR(1),
    using_cheats VARCHAR(1),
    FOREIGN KEY (player_id) REFERENCES users (id)
);