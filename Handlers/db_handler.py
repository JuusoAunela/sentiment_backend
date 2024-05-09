import os
from dotenv import load_dotenv
from supabase import Client, create_client
from supabase.client import ClientOptions
from Handlers import sentiment_handler as sh

# Load .env
load_dotenv()

# Get the url from .env
db_url = os.environ.get('DB_URL')
# Get the key from .env
db_key = os.environ.get('DB_KEY')

# Create client
supabase: Client = create_client(
    db_url, 
    db_key,
  options=ClientOptions(
    postgrest_client_timeout=10,
    storage_client_timeout=10,
    schema="public",
  ))

# Get all reviews from supabase
def get_all():
    result = supabase.table('feedback').select(
        'feedback, sentiment_id:sentiment (sentiment, confidence, subjectivity), ' + 
        'customer_id:customer (name, email)').execute()
    return result.data

# Submit new data to supabase
def submit_new(data):
    print(data)
    # Add new customer to the db
    customer = submit_customer(data)
    # Analyse the feedback
    feedback = data.json['feedback']
    analysis = sh.response_all(feedback)
    # Add new sentiment to the db
    sentiment = submit_sentiment(analysis)

    # Get the id's for foreignkeys
    customer_id = customer[0]['id']
    sentiment_id = sentiment[0]['id']

    # Add new review to the db
    new_entry = supabase.table('feedback').insert({
        'feedback': feedback, 'customer_id': customer_id, 'sentiment_id': sentiment_id
    }).execute()

    return new_entry.data

# Add new customer to the db
def submit_customer(data):
    new_customer = supabase.table('customer').insert(
        {'name': data.json['name'], 'email': data.json['email']}).execute()
    return new_customer.data

# Add new sentiment to the db
def submit_sentiment(data):
    new_sentiment = supabase.table('sentiment').insert({
        'sentiment': data['sentiment'], 'confidence': data['polarity'], 
        'subjectivity': data['subjectivity']}).execute()
    return new_sentiment.data

def format_feedback(data):
    response = []
    row = []
    # Format the data
    for item in data:
        row.append(item['feedback'])
        row.append(item['sentiment_id']['sentiment'])
        row.append(round(item['sentiment_id']['confidence'], 2))
        # Appraise the objectivity and format it to a string
        objecttivity = sh.appraise_subjectivity(item[
            'feedback']) + ' (' + str(round(
                item['sentiment_id']['subjectivity'], 2)) + ')'
        row.append(objecttivity)
        row.append(item['customer_id']['name'])
        row.append(item['customer_id']['email'])
        response.append(row)
        row = []

    return response