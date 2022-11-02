import numpy as np
import pandas as pd
import nltk

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
# read input file
data = pd.read_csv('reddit_scraped_movie_comments.csv')

# remove punctuation, numbers, special characters
# https://python.plainenglish.io/text-preprocessing-in-natural-language-processing-in-python-8aeb7bfdaee7
data["body"] = data['body'].str.replace("https?://[^\s\n\r]+", " ")
data['title_cleaned'] = data['title'].str.replace("https?://[^\s\n\r]+", " ")

data["body"] = data['body'].str.replace("[^a-zA-Z#]", " ")
data["title_cleaned"] = data['title_cleaned'].str.replace("[^a-zA-Z#]", " ")

data["body"] = data['body'].str.replace("[0-9]+", " ")
data["title_cleaned"] = data['title_cleaned'].str.replace("[0-9]+", " ")

data['body_polarity'] = 0
data['title_polarity'] = 0
# lowercase
for index, row in data.iterrows():
    row['body'] = (str(row['body']).lower())
    row['title_cleaned'] = (str(row['title_cleaned']).lower())
    # remove short words
    row["body"] = ' '.join([w for w in row['body'].split() if len(w) > 2])
    row["title_cleaned"] = ' '.join([w for w in row['title_cleaned'].split() if len(w) > 2])

    # lemmatizer
    # https://www.machinelearningplus.com/nlp/lemmatization-examples-python/
    row['body'] = ' '.join([lemmatizer.lemmatize(w) for w in row['body'].split()])
    row['title_cleaned'] = ' '.join([lemmatizer.lemmatize(w) for w in row['title_cleaned'].split()])

    # remove stop words
    # https://towardsdatascience.com/text-pre-processing-stop-words-removal-using-different-libraries-f20bac19929a
    row['body'] = ' '.join([word for word in row['body'].split() if word.lower() not in sw_nltk])
    row['title_cleaned'] = ' '.join([word for word in row['title_cleaned'].split() if word.lower() not in sw_nltk])



    if len(row['body']) != 0:
        data.at[index, 'body'] = row['body']
        data.at[index, 'body_polarity'] = sia.polarity_scores(row['body'])['compound']
    if len(row['title_cleaned']) != 0:
        data.at[index, 'title_cleaned'] = row['title_cleaned']

#
# data.dropna(subset=["text"], inplace=True)

data.to_csv(index=False, path_or_buf="reddit_data/cleaned_reddit_comments.csv")
