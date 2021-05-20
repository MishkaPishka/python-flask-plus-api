import werkzeug.exceptions
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import json

from werkzeug.security import generate_password_hash

from flaskr import db_queries
from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('user', __name__)

import  auth

@bp.errorhandler(werkzeug.exceptions.Unauthorized)
def handle_bad_credentials_request(e):
    print(e)
    return e.description, 403

bp.register_error_handler(403, handle_bad_credentials_request)

@bp.route('/user')
@login_required
def user_page():
    if  g.user == None:
        print("user is either not in system or not logged in")
        return redirect(url_for('blog.index'))

    db = get_db()
    user = db_queries.get_user_by_name(db,g.user['username'],with_pass = False)
    user_generated_text_data = db_queries.get_generated_text_plus_feedback_by_user_id(db,user['id'])
    user_twitter_classification_plus_feedback = db_queries.twitter_classification_plus_feedback_by_user_id(db,user['id'])



    return render_template('user/user.html',user=user,generated_text_data_table= user_generated_text_data,twitter_classification_plus_feedback_table=user_twitter_classification_plus_feedback )







def parse_update_details_requrst(form):
    reply = []
    if len(form['newPassword']) >0 : reply.append(['hashed_password',  generate_password_hash(form['newPassword'])])

    [reply.append([i,j]) for i,j in form.items() if len(j)>0 and len(j)<50 and i not in ['username','password','newPassword']]
    return reply


@bp.route('/user/delete_history',methods=['POST'])
@login_required
def delete_search_history():
    db_queries.delete_history_by_author_id(get_db(),g.user['id'])


    return {"data":"OK"}


@bp.route('/user/update',methods=['POST'])
@login_required
def change_details():
    # dict([(x,g.user[x]) for x in g.user.keys()])
    if  not auth.valid_credentials(g.user,request.form['password']):  abort(403, description="Invalid credentials")
    if request.form['username'] != g.user['username']:  abort(403, description="Cannot change username")
    try:
        db_queries.update_user_details(get_db(),g.user, parse_update_details_requrst(request.form))
        return {"data":"UPDATE COMPLETE"}
    except Exception as er:
        print(er.text)
        return {"Error",404}
   # except Exception as e: return e.message,405





