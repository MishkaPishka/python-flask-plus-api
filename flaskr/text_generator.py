from flask import (
    Blueprint, render_template, request, flash, session
)

from flaskr import validator_
from flaskr.auth import login_required

import flaskr.resources.text_data   as  d
import service_requests as c
from flaskr.db import get_db
from flaskr.validator_ import  GenTextRequestForm, FeedbackGenTextValidation

bp = Blueprint('text-gen', __name__)
import db_queries


### RENDER PAGE
@bp.route('/text-gen',methods=['GET'])
def generate_text_page():
    return render_template('service/text_generator_view.html', project_title=d.TEXT_GENERATOR_TITLE, project_description=d.TEXT_GENERATOR_DESCRIPTION)


### RETURN THE GENERATED TEXT
#TODO - create a new rout + in a get method
@bp.route('/text-gen',methods=['POST'])
def generate_text_request():
    reply = handle_generate_text_request(request.form)
    return reply


def handle_generate_text_request(form):
    if form is None or not   GenTextRequestForm(form).validate():   return "Invalid parameters",405
    text_response= c.text_gen_api_request(request.form['seed'],request.form['method'],request.form['output_length']).text
    return text_response

@bp.route('/text-gen/rank',methods=['POST'])
@login_required
#TODO
def submit_feedback():
    if request.form is None or not   FeedbackGenTextValidation(request.form).validate() :   return "Invalid parameters",405
    #save in db
    try :
        db_result = db_queries.add_feedback_on_generated_text_to_db(get_db(), request.form, session['user_id'])
        return {'data':'Feedback successful'}
    except  Exception as err :
        print(err)
        return err,err.code

