from flask import Flask, request
from Services import sentiment_service, db_service

app = Flask(__name__)

# Set CORS off
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response



# Test route
@app.route('/')
def index():
    return 'Hello World!'

# Return sentiment analysis result
@app.route('/sentiment', methods=['POST'])
def sentiment_analysis():
    return sentiment_service.sentiment(request)

@app.route('/feedback', methods=['OPTIONS', 'POST'])
def feedback():
    if request.method == 'OPTIONS':
        return '', 200  # Empty response with OK status code
    # Existing logic for handling POST requests to /feedback
    return db_service.submit_new(request)


@app.route('/review', methods=['GET'])
def listing():
    return db_service.get_all()
    

if __name__ == '__main__':
    #run at localhost
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=8080)