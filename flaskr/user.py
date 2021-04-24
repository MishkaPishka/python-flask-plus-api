from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import json

from flaskr import db_queries
from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('user', __name__)


@bp.route('/user')
@login_required
def user_page():
    if  g.user == None:
        print("user is either not in system or not logged in")
        return redirect(url_for('blog.index'))

    db = get_db()

    user = db_queries.get_user_by_name(db,g.user['username'],with_pass = False)


    return render_template('user/user.html',user=user )


@bp.route('/user',methods=['UPDATE'])
@login_required
def change_details():
    username = request.form['username']

    password = request.form['password']
    new_password = request.form['newPassword']


    [(x,request.form[x]) for x in request.form.keys()]
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    about = request.form['about']
    update_values = {}

    #check user is valid
        #a - user id
        # password matches
    if  g.user == None:
        print("user is either not in system or not logged in")
        return redirect(url_for('blog.index'))

        db = get_db()

    user = db_queries.get_user_by_name(db,g.user['username'])


    verified_user = check_user_varifies(g.user,user, password)
    if not verified_user:
        return {'ERROR':'INVALID USER CREDENTIALS '}

    #update user data

    x = json.dumps([print (ix) for ix in user])  # CREATE JSON


    ### TODO
    #get user , get user tweet search, get user rankings
    tweet_history = db_queries.get_tweet_from_db_by_user(db,user.id)
    feedback_history = db_queries.get_feedback_by_user(db,user.id)

    return render_template('user/user.html',user=user,tweet_history=tweet_history,feedback_history=feedback_history )






