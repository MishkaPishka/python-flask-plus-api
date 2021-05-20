import flaskr.db
from flaskr import db
from flaskr.resources import text_data


def get_user_by_id(db,id):
    return db.execute(
        'Select * from user where id = ? ', (id,)

    ).fetchone()


def get_generated_text_plus_feedback_by_user_id(db,id):

    return db.execute(
        'Select  * from generated_text_plus_feedback where author_id = ?',(id,)

    ).fetchall()

def twitter_classification_plus_feedback_by_user_id(db,id):
    return db.execute(
        'Select  * from twitter_classification_plus_feedback where author_id = ?', (id,)

    ).fetchall()

# 'Select  generated_text_plus_feedback.* from generated_text_plus_feedback join user on author_id = user.id where author_id = ? ', (
# id,)


def get_user_by_name(db,username,with_pass=False):
    return  db.execute(
        'Select  * from user where username = ? ',(username,)

    ).fetchone()


def update_user_data(data):
    pass
def add_new_user(user):
    pass

def get_searches_by_user(user):
    pass


def insert_new_user (username, hashed_password,fname,lname,email,about):
    pass


def update_user_details(db,g_user,details):


    update_str = 'UPDATE user SET '+''.join([x[0]+' = "'+ x[1]+'", '  for x in details])+ 'username="'+ g_user['username']+'" where username like "'+g_user['username']+'";'
    print(update_str)
    db.execute(update_str)
    db.commit()
    return True

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


def get_user_field_by_username(db,username,fieldname):
     return db.execute(
        'Select  * from user where username = ? ', (username,)

    ).fetchone()[fieldname]


def delete_history_by_author_id(db,id):
    try:
        db.execute("DELETE FROM generated_text_plus_feedback  where generated_text_plus_feedback.author_id=?", (id,))
        db.execute(
            "DELETE FROM twitter_classification_plus_feedback  where twitter_classification_plus_feedback.author_id=?",
            (id,))
        db.execute("commit")
        return True
    except Exception:
        print("failed!")
        db.execute("rollback")
        return False
    # db.execute(
    #     # 'DELETE  from twitter_classification_plus_feedback where author_id = ? ', (id)
    # 'DELETE generated_text_plus_feedback , twitter_classification_plus_feedback FROM generated_text_plus_feedback INNER JOIN twitter_classification_plus_feedback WHERE  generated_text_plus_feedback.author_id= ? and twitter_classification_plus_feedback.author_id = ?',(id,id,)
    #
    # )
    # db.commit();

def add_feedback_on_tweet_classification_to_db(db, form, user_id):
    tweet = form['tweet_to_classify']
    classification = form['classification_result']
    feedback = form['result_feedback']
    db.execute(
     "INSERT into twitter_classification_plus_feedback (author_id,data,classification,user_feedback)  VALUES (?, ?,?,?)",
        (user_id, tweet, feedback, classification)
    )


    db.commit()

#TODO

def add_feedback_on_generated_text_to_db(db, form, user_id):
    # form['data[seed]'], form['data[length]'],form['data[method]'],form['data[output]'],form['data[rank]']
    # classification = form['classification_result']
    # feedback = form['result_feedback']
    # text = form['output']
    db.execute(
     "INSERT into generated_text_plus_feedback (author_id,param_method,param_length,param_output_size,seed,data,score)   VALUES (?, ?,?,?,?,?,?)",
        (user_id,  text_data.GENERATION_METHOD[ form['data[method]']],len(form['data[seed]']),len(form['data[seed]']),form['data[seed]'], form['data[output]'], form['data[ranking]'])
    )

    db.commit()

