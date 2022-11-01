import numpy as np

import pandas as pd
import re
import matplotlib.pyplot as plt
import string
import nltk
from nltk.stem.porter import *

stemmer = PorterStemmer()
import string

string.punctuation
# read input file
data = pd.read_csv('reddit_scraped_movie_comments.csv')

# remove punctuation, numbers, special characters
data["body"] = data['body'].str.replace("[^a-zA-Z#]", " ")
data["title_cleaned"] = data['title'].str.replace("[^a-zA-Z#]", " ")

# https://python.plainenglish.io/text-preprocessing-in-natural-language-processing-in-python-8aeb7bfdaee7
data["body"] = data['body'].str.replace("https?://[^\s\n\r]+", " ")
data["title_cleaned"] = data['title_cleaned'].str.replace("https?://[^\s\n\r]+", " ")

data["body"] = data['body'].str.replace("[0-9]+", " ")
data["title_cleaned"] = data['title_cleaned'].str.replace("[0-9]+", " ")

# lowercase
# for index, row in data.iterrows():
#     row['body'] = (str(row['body']).lower())
#     row['title_cleaned'] = (str(row['title_cleaned']).lower())
#     # remove short words
#     row["body"] = ' '.join([w for w in row['body'].split() if len(w) > 2])
#     row["title_cleaned"] = ' '.join([w for w in row['title_cleaned'].split() if len(w) > 2])
#
#     # stemmer
#     row['body'] = ' '.join([stemmer.stem(w) for w in row['body'].split()])
#     row['title_cleaned'] = ' '.join([stemmer.stem(w) for w in row['title_cleaned'].split()])
#
#     # lemmatizer
#
#     data['body'] = row['body']
#     data['title_cleaned'] = row['title_cleaned']

#
# data.dropna(subset=["text"], inplace=True)

data.to_csv(index=False, path_or_buf="reddit_data/cleaned_reddit_comments.csv")
