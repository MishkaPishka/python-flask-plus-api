from flask import (
    Blueprint, render_template, request, flash, session
)
from flaskr.auth import login_required

import flaskr.resources.text_data   as  d
import service_requests as c
bp = Blueprint('text-gen', __name__)
import db_queries
MAX_SEED_LEN = 10
MAX_OUTPUT_LEN = 1000

### RENDER PAGE
@bp.route('/text-gen',methods=['GET'])
def generate_text_page():
    return render_template('service/text_generator_view.html', project_title=d.TEXT_GENERATOR_TITLE, project_description=d.TEXT_GENERATOR_DESCRIPTION)


### RETURN THE GENERATED TEXT
@bp.route('/text-gen',methods=['POST'])
def generate_text_request():
    reply = handle_generate_text_request(request.form)
    return reply


def handle_generate_text_request(form):
    if form is None or 'seed' not in form.keys() or 'length' not in form.keys():
        return "Invalide Request",405
    elif len(form['seed'])>MAX_SEED_LEN or int(form['length']) > MAX_OUTPUT_LEN:
        return "Invalid parameters",405
    else:
        return c.text_gen_api_request(request.form['seed'],request.form['length'],request.form['method'])


@bp.route('/text-gen/rank',methods=['POST'])
@login_required
def submit_feedback():
    form  = request.form
    user_id = session['id']
    #save in db
    try : return db_queries.save_feedback_in_db(form,user_id),200

    except  Exception as err :
        print(err)
        return err,err.error_code

