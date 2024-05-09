from flask import request
from Handlers import sentiment_handler as sh
from Handlers import db_handler as dbh

def sentiment(data):
    # get sentence
    feedback = data.json['feedback']

    # check if sentence is valid
    if feedback and len(feedback) > 0:
        sentiment = sh.response_sentiment(feedback)
        return sentiment
    # else return error
    else:
        # TODO: handle error
        return 'Error: Invalid feedback'