# This file contains the addresses for remote services the app used.
# At the moment - text generation and classification
import requests

GEN_TEXT_SERVICE_BASE_URL_GET = 'http://127.0.0.1:5002/?'
TWITTER_CLASSIFIER_BASE_URL = 'http://127.0.0.1:5002/'

GET_TEET_FORMAT = ''
CLASSIFY_TWEET_FORMAT = ''
FEEDBACK_SERVICE_FORMAT = ''


def text_gen_api_request(seed,length,method):
    function_to_be_used = request_wrapper(requests.get)
    return function_to_be_used(GEN_TEXT_SERVICE_BASE_URL_GET, {'seed': seed,'length':length,'method':method})


def get_twitter_by_username_request(twitter_username):
    # function_to_be_used = request_wrapper(requests.get)
    # function_to_be_used(TWITTER_CLASSIFIER_BASE_URL+GET_TEET_FORMAT,  "query_value={}&max_results=10&type=name".format(twitter_username)).json()
    # ## TODO -- ADD DATA or format reply
    function_to_be_used = request_wrapper(requests.get)
    return function_to_be_used(GEN_TEXT_SERVICE_BASE_URL_GET, "query_value={}&max_results=10&type=name".format(twitter_username))

    # try:
    #     requests.get(TWITTER_CLASSIFIER_BASE_URL+GET_TEET_FORMAT,  "query_value={}&max_results=10&type=name".format(twitter_username)).json()
    # except Exception as err:
    #     print('get_twitter_by_username_request',err)
    #     #RETURN MOK UPS
    #     a = 'bbbbbb'
    #     a = 'bbbbbb'
    #     x = a *10
    #     return {"data":x}


def classify_tweet(tweet):
    function_to_be_used = request_wrapper(requests.get)
    return function_to_be_used(TWITTER_CLASSIFIER_BASE_URL + GET_TEET_FORMAT,
                     "query_value={}&max_results=10&type=name".format(tweet))


def send_feedback_on_tweet_classification(tweet,classification,feedback,user):
    function_to_be_used = request_wrapper(requests.post)
    return function_to_be_used(TWITTER_CLASSIFIER_BASE_URL + FEEDBACK_SERVICE_FORMAT,
                               {'tweet':tweet,'classification':classification,'feedback':feedback,'user':user})


def request_wrapper(func):
    def add_try_catch(*args, **kwargs):
        try:
            return  func(*args, **kwargs)

        except Exception as err:
            print("Error in {}".format(func.__name__), err)
            # return {'data':'blabla'}
            return "service error",420

    return add_try_catch