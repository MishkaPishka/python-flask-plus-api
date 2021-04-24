--s
--User, User Query,User Texts, Success Rates..
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS tweet;
DROP TABLE IF EXISTS generatedText;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  hashed_password TEXT NOT NULL,
  fname TEXT  ,
  lname TEXT  ,
  email TEXT  ,
  about TEXT
);

CREATE TABLE tweet (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE classifications (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  data TEXT,
  classification Text
  FOREIGN KEY (author_id) REFERENCES user (id)
)

CREATE TABLE rankings (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  param_method = INTEGER,
  param_length = INTEGER,
  param_output_size = INTEGER,
  data TEXT,
  classification TEXT,
  score INTEGER
  FOREIGN KEY (author_id) REFERENCES user (id)

)
CREATE TABLE generatedText (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  body TEXT NOT NULL,
  seed TEXT,
  result TEXT,
  FOREIGN KEY (author_id) REFERENCES user (id)
);


CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

