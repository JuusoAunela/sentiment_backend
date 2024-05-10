from flask import request
from Handlers import sentiment_handler as sh
from Handlers import db_handler as dbh

def sentiment(data):
    return sh.response_sentiment(data)