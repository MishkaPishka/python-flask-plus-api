from flaskr import db


def get_user_by_id(db,id):
    return db.execute(
        'Select * from user where id = ? ', (id)

    ).fetchone()

def get_user_by_name(db,username,with_pass=False):
    return  db.execute(
        'Select  * from user where username = ? ',(username)

    ).fetchone()


def update_user_data(data):
    pass
def add_new_user(user):
    pass

def get_searches_by_user(user):
    pass


def insert_new_user (username, hashed_password,fname,lname,email,about):
    pass
def update_user_details (username, hashed_password,fname,lname,email,about):
    pass

def add_tweet_to_db (request_tweet,respnse_tweet,user_id,data):
    pass


def get_tweet_from_db_by_user (user_id):
    pass

def add_tweeter_classification_request (tweet,result,user_id,tag,feedback):
    pass

def get_all_tweeter_classification_request ():
    pass

def get_tweeter_classification_request_by_user (user_id):
    pass

def get_user_activity_data (user_id):
    pass

def save_feedback_in_db(feedback,user):
    pass;

