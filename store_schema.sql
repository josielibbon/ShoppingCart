PRAGMA foreign_keys=off;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  username        varchar(50) not null PRIMARY KEY,
  password        varchar(50) not null,
  name            varchar(50) not null
);

DROP TABLE IF EXISTS games;
CREATE TABLE games (
  title        varchar(32) not null PRIMARY KEY,
  price        int(5) not null,
  type         varchar(50) not null,
  quantity     int(5) not null
);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
  title        varchar(32) not null,
  price        int(5) not null,
  type         varchar(50) not null,
  quantity     int(5) not null
);

DROP TABLE IF EXISTS gametypes;
CREATE TABLE gametypes (
  type         varchar(50) not null
);

PRAGMA foreign_keys=on;

-- users
INSERT INTO users VALUES ('testuser', 'testpass', 'Test User');
  
-- games
INSERT INTO games VALUES ('Zelda', 60, 'Nintendo', 2);
INSERT INTO games VALUES ('Spiderman', 50, 'PS4', 4);
INSERT INTO games VALUES ('Mariokart', 40, 'Nintendo', 7);
INSERT INTO games VALUES ('Xenoblade', 40, 'Nintendo', 7);
INSERT INTO games VALUES ('Batman', 40, 'PS4', 7);
INSERT INTO games VALUES ('Borderlands', 40, 'PS4', 7);
INSERT INTO games VALUES ('Doom', 40, 'XBox', 7);
INSERT INTO games VALUES ('Cupheads', 40, 'XBox', 7);
INSERT INTO games VALUES ('Fortnite', 40, 'XBox', 7);
INSERT INTO games VALUES ('Halo', 40, 'PS4', 7);

-- gametypes
INSERT INTO gametypes VALUES ('Nintendo');
INSERT INTO gametypes VALUES ('PS4');
INSERT INTO gametypes VALUES ('XBox');

