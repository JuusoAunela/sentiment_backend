from flask import Flask, request
import sentiment_analysis as sa

app = Flask(__name__)

# Test route
@app.route('/')
def index():
    return 'Hello World!'

# Return sentiment analysis result
@app.route('/sentiment', methods=['POST'])
def sentiment():
    # get sentence from request
    sentence = request.json['sentence']

    # check if sentence is valid
    if sentence and len(sentence) > 0:
        return sa.get_sentiment(sentence)
    # else return error
    else:
        # TODO: handle error
        return 'Error: Invalid sentence'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)