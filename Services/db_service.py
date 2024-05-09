from Handlers import db_handler as dbh

def get_all():
    # Get all data from supabase
    data = dbh.get_all()
    return dbh.format_feedback(data)

def submit_new(data):
    # Submit new data to supabase
    return dbh.submit_new(data)

def get_all_feedbacks():
    # TODO Get all feedbacks from supabase
    return True

def get_all_sentiment():
    # TODO Get all sentiment from supabase
    return True

def get_all_subjectivity():
    # TODO Get all subjectivity from supabase
    return True
