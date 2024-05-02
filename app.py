from flask import Flask, request
import sentiment_analysis as sa

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/sentiment', methods=['POST'])
def sentiment():
    sentence = request.json['sentence']

    if sentence and len(sentence) > 0:
        return sa.get_sentiment(sentence)
    else:
        return 'Negative'

if __name__ == '__main__':
    app.run(debug=True)