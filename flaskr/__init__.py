import os
from datetime import timedelta

from flask import Flask,session


import  db
import auth
import blog
import user

import text_generator
import twitter_classification
from flaskr import about


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # SECRET_KEY='fgsdff',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    #ADDED - https://stackoverflow.com/questions/41278418/how-to-add-session-timeout-but-keep-session-alive-with-user-activity-in-flask
    app.permanent_session_lifetime = timedelta(minutes=2)
    app.config.from_mapping(
        # SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )


    # TODO
    #  use random value for secret key
    #
    if test_config is None:
        # load the instance config, if it exists, when not testing
        # app.config.from_pyfile('config.py', silent=True)
        app.config.from_pyfile('configuration.cfg', silent=True)

    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # from . import db
    db.init_app(app)

    # from . import auth
    app.register_blueprint(auth.bp)

    # from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')


    app.register_blueprint(user.bp)
    app.register_blueprint(twitter_classification.bp)
    app.register_blueprint(text_generator.bp)

    app.register_blueprint(about.bp)


    # # a simple page that says hello
    # @app.route('/hello')
    # def hello():
    #     return 'Hello, World!'

    return app


# Further file processing goes here
if __name__ == '__main__':

    app = create_app()
    print('app.debug == True',app.debug == True)

    ##TO INITIATE DB WHEN USING DEBUG MODE
    # with app.app_context():
    #     # within this block, current_app points to app.
    #     db.init_db()
    # exit(0)
    app.run()

    # app.run(port=5001)

    # app.run(debug=True)


