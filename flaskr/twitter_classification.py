from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify,session
)
import flaskr.resources.text_data   as  text_data
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
import requests
import service_requests as c
import db_queries
from flaskr.validator_ import FeedbackClassifyTweet

bp = Blueprint('twitter-classification', __name__)



@bp.route('/twitter-classification')
@login_required
def twitter_classification_page():
    return render_template('service/classify_twitter_view.html', project_title=text_data.CLASSIFY_TWITTER_TITLE, project_description=text_data.CLASSIFY_TWITTER_DESCRIPTION)

@bp.route('/twitter-classification/get-tweet-by-username/<twitter_username>',methods = [ 'GET'])
@login_required
def get_tweet(twitter_username):
    #PARSE
    #MAKE REQUEST
    #RETURN
    #USER TWITTER SERTVICE TO GET DATA
    return {"data":"bla!!!"}
    reply   =   c.get_twitter_by_username_request(  twitter_username)

    return reply




@bp.route('/twitter-classification/classification-request/<tweet>',methods = [ 'GET'])
@login_required
def classify_tweet(tweet):
    return  c.classify_tweet(  tweet)


#TODO
@bp.route('/twitter-classification/give-feedback-on-tweet-classification/',methods = [ 'POST'])
@login_required
def giveFeedbackOnTweetClassification():
    if (request.form is None or not     FeedbackClassifyTweet(request.form).validate()): return "Invalid parameters",405
    try:
        db_queries.add_feedback_on_tweet_classification_to_db(get_db(),request.form, session['user_id'])
        return {"data":'Done'}
    except Exception as e:
        return e,405







