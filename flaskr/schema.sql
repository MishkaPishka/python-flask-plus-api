--s
--User, User Query,User Texts, Success Rates..
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS tweet;
DROP TABLE IF EXISTS generated_text_plus_feedback;
DROP TABLE IF EXISTS twitter_classification_plus_feedback;

CREATE TABLE  IF NOT EXISTS user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  hashed_password TEXT NOT NULL,
  fname TEXT  ,
  lname TEXT  ,
  email TEXT  ,
  about TEXT
);

CREATE TABLE  IF NOT EXISTS tweet (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);


CREATE TABLE  IF NOT EXISTS twitter_classification_plus_feedback (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  data TEXT NOT NULL,
  classification INTEGER,
  user_feedback INTEGER,
  FOREIGN KEY (author_id) REFERENCES user (id)

);

CREATE TABLE  IF NOT EXISTS generated_text_plus_feedback (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  param_method  INTEGER,
  param_length  INTEGER,
  param_output_size  INTEGER,
  seed TEXT,
  data TEXT,
  score INTEGER,


  FOREIGN KEY (author_id) REFERENCES user (id)

);


CREATE TABLE  IF NOT EXISTS post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

