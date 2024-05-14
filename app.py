from flask import Flask, request
from Services import sentiment_service, db_service
from Handlers import sentiment_handler

app = Flask(__name__)

# Set CORS off
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

#@app.before_request
#def run_on_start():
#    training_handler.basic_training()

# Test route
@app.route('/')
def index():
    return 'Hello World!'

# Return sentiment analysis result
@app.route('/sentiment', methods=['OPTIONS','POST'])
def sentiment_analysis():
    if request.method == 'OPTIONS':
        return '', 200
    sentence = request.json['sentence']
    return sentiment_service.sentiment(sentence)

@app.route('/feedback', methods=['OPTIONS', 'POST'])
def feedback():
    if request.method == 'OPTIONS':
        return '', 200  # Empty response with OK status code
    # Existing logic for handling POST requests to /feedback
    return db_service.submit_new(request)


@app.route('/review', methods=['GET'])
def listing():
    return db_service.get_all()

@app.route('/test', methods=['OPTIONS', 'POST'])
def test():
    if request.method == 'OPTIONS':
        return '', 200
    #sentiment = sentiment_handler.cl_sentiment(request.json['sentence'])
    #probability = sentiment_handler.cl_probability(request.json['sentence'])
    #return sentiment.jsonify(sentiment=sentiment, probability=probability)
    return sentiment_handler.cl_probability(request.json['sentence'])

if __name__ == '__main__':
    # run at localhost
    app.run(debug=False)
    # run live
    # app.run(host='0.0.0.0', port=8080)