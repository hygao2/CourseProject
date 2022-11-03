import praw
import pandas as pd
from config import *

reddit = praw.Reddit(client_id=reddit['my_client_id'],
                     client_secret=reddit['my_client_secret'],
                     user_agent=reddit['my_user_agent'])

def movie_comments(movie, subreddit, limit):
    list = []
    for post in subreddit.search(movie, limit=limit):
        post.comments.replace_more(limit=0)
        all_comments = post.comments.list()
        for comment in all_comments:
            list.append([comment.id, comment.submission.title, comment.body, comment.score, comment.created_utc])
    return list

sub1 = "movies"
sub2 = "MovieDetails"
combined_string = sub1 + "+" + sub2
combined_sub = reddit.subreddit(combined_string)

movie = "The Dark Knight"
limit = 5

comments = movie_comments(movie, combined_sub, limit)
print('finished comments')

df = pd.DataFrame(comments, columns=['title', 'id', 'body', 'score', 'created'])
df.to_csv('reddit_data/reddit_scraped_movie_comments.csv')
