import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr import db_queries
from flaskr.db import get_db
print("In routes, auth.pyh:",__name__)

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        about = request.form['about']

        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif \
                db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, hashed_password,fname,lname,email,about) VALUES (?, ?,?,?,?,?)',
                (username, generate_password_hash(password), fname, lname, email,about)
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)
    if 'next' in request.args:
        return redirect(next)
    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db_queries.get_user_by_name(db,username)
        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['hashed_password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            if 'next' in request.args:
                return redirect(request.args['next'])
            return redirect(url_for('index'))

        flash(error)

    if 'url' in session:
        return redirect(session['url'])


    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():

    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            # g.setdefault('from',request.url)
            return redirect(url_for('auth.login',next=request.url))

        return view(**kwargs)

    return wrapped_view


