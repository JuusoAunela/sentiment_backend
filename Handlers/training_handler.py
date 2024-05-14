import pandas as pd
from textblob.classifiers import NaiveBayesClassifier

def basic_training():
    # Read the dataset
    df = pd.read_csv('./Training/Restaurant reviews.csv')

    # Remove all Like and null values
    df = df.dropna(subset=['Rating'])
    df = df[df['Rating'] != 'Like']

    # Change Rating type to float
    df['Rating'] = df['Rating'].astype(float)

    # create sentiment column, 1-2 = neg, 4-5 = pos
    df['sentiment'] = df['Rating'].apply(lambda x: 'Neg' if x<=3 else 'Pos')

    # Drop nulls from review
    df = df.dropna(subset=['Review'])

    # Drop all other columns except review and sentiment
    df = df[['Review', 'sentiment']]

    # create tuple of the df
    training_data = []
    for index, row in df.iterrows():
        training_data.append((row['Review'], row['sentiment']))
    print(training_data[0])
    # Create classifier
    classifier = NaiveBayesClassifier(training_data)
    test_text = 'I love the food!'
    # classifier.accuracy(test_text)
    print(classifier.classify(test_text))
    return classifier
