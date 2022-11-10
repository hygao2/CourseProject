import numpy as np
import pandas as pd
import nltk

nltk.download('stopwords')
nltk.download('omw-1.4')
nltk.download('wordnet')
nltk.download('vader_lexicon')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

sw_nltk = stopwords.words('english')
sw_nltk.remove('not')

from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
# Init the Wordnet Lemmatizer
lemmatizer = WordNetLemmatizer()
import string

string.punctuation


def preprocess():
    # read input file
    data = pd.read_csv('../reddit_data/reddit_scraped_movie_comments.csv')

    # remove punctuation, numbers, special characters
    # https://python.plainenglish.io/text-preprocessing-in-natural-language-processing-in-python-8aeb7bfdaee7
    data["body"] = data['body'].str.replace("https?://[^\s\n\r]+", " ")
    data["body"] = data['body'].str.replace("[^a-zA-Z#]", " ")
    data["body"] = data['body'].str.replace("[0-9]+", " ")

    # lowercase
    for index, row in data.iterrows():
        row['body'] = (str(row['body']).lower())
        # remove short words
        row["body"] = ' '.join([w for w in row['body'].split() if len(w) > 2])

        # lemmatize
        # https://www.machinelearningplus.com/nlp/lemmatization-examples-python/
        row['body'] = ' '.join([lemmatizer.lemmatize(w) for w in row['body'].split()])

        # remove stop words
        # https://towardsdatascience.com/text-pre-processing-stop-words-removal-using-different-libraries-f20bac19929a
        row['body'] = ' '.join([word for word in row['body'].split() if word.lower() not in sw_nltk])

        data.at[index, 'body'] = row['body']
        # sentiment scores
        data.at[index, 'neg'] = sia.polarity_scores(row['body'])['neg']
        data.at[index, 'neu'] = sia.polarity_scores(row['body'])['neu']
        data.at[index, 'pos'] = sia.polarity_scores(row['body'])['pos']
        data.at[index, 'compound'] = sia.polarity_scores(row['body'])['compound']

    data.to_csv(index=False, path_or_buf="../reddit_data/cleaned_reddit_comments.csv")


def calculate_avg_sentiment():
    data = pd.read_csv('../reddit_data/cleaned_reddit_comments.csv')
    return np.mean(data['compound'])
