from textblob import TextBlob

# sentiment analysis from previous task assignment

# Analyze the polarity of the sentence
def get_polarity(text):
  return str(TextBlob(text).sentiment.polarity)

# Analyze the subjectivity of the sentence
def get_subjectivity(text):
  return str(TextBlob(text).sentiment.subjectivity)

# Analyze the sentiment of the sentence
def get_sentiment(text):
  # Sentence is positive
  if TextBlob(text).sentiment.polarity > 0.25:
    return "Positive"
  # Sentence is negative
  elif TextBlob(text).sentiment.polarity < -0.25:
    return "Negative"
  # Sentence is neutral
  else:
    return "Neutral"
  
# Return JSON object of full analysis
def response_all(text):
  return {
    "polarity": get_polarity(text),
    "subjectivity": get_subjectivity(text),
    "sentiment": get_sentiment(text)
  }

# Return polarity analysis result in JSON
def response_polarity(text):
  return {
    "polarity": get_polarity(text),
    "sentiment": get_sentiment(text)
  }

# Return subjectivity analysis result in JSON
def response_subjectivity(text):
  return {
    "subjectivity": get_subjectivity(text),
    "sentiment": get_sentiment(text)
  }

# Return sentiment analysis result in JSON
def response_sentiment(text):
  return {
    "sentiment": get_sentiment(text)
    }