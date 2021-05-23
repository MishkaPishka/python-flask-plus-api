from flask_restful import inputs
from validator import validate_many

from flaskr.resources import text_data

from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField

from flaskr.resources.text_data import GENERATION_METHOD, MAX_TEXT_GEN_OUTPUT, MAX_SEED_LEN, MAX_PREFIX_LEN


class GenTextRequestForm(Form):
    seed = StringField('seed', [validators.Length(min=1, max=MAX_SEED_LEN)])
    method = StringField('method', [validators.AnyOf(GENERATION_METHOD.keys())])
    # output_length = IntegerField('output_length', [validators.number_range(min=1, max=MAX_TEXT_GEN_OUTPUT)])




class RegisterationForm(Form):
    pass
class SigninForm(Form):
    pass
class GetTweetForm(Form):
    pass
class ClassifyTweetForm(Form):
    pass


class FeedbackClassifyTweet(Form):
    tweet_to_classify = StringField('tweet_to_classify', [validators.length(min=1, max=200)])
    classification_result = IntegerField('tweet_to_classify', [validators.number_range(min=0, max=1)])
    result_feedback = IntegerField('result_feedback', [validators.number_range(min=0, max=1)])



class FeedbackGenTextValidation(Form):

    seed = StringField('data[seed]', [validators.length(min=1, max=11)])
    length = IntegerField('data[length]', [validators.number_range(min=1, max=MAX_TEXT_GEN_OUTPUT)])
    method = StringField('data[method]', [validators.AnyOf(GENERATION_METHOD.keys())])
    output = StringField('data[output]', [validators.Length(min=1,max=MAX_TEXT_GEN_OUTPUT)])
    ranking = IntegerField('data[ranking]', [ validators.number_range(min=0,max=5)])
    def validate(self):
        return True;
