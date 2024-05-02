from textblob import TextBlob

def get_polarity(text):
  return str(TextBlob(text).sentiment.polarity)

def get_subjectivity(text):
  return str(TextBlob(text).sentiment.subjectivity)

def get_sentiment(text):
  if TextBlob(text).sentiment.polarity > 0.25:
    return "Positive"
  elif TextBlob(text).sentiment.polarity < -0.25:
    return "Negative"
  else:
    return "Neutral"