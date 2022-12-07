import praw
import pandas as pd
from config import *

reddit = praw.Reddit(client_id=reddit['my_client_id'],
                     client_secret=reddit['my_client_secret'],
                     user_agent=reddit['my_user_agent'])

def movie_comments(movie):
    sub1 = "movies"
    sub2 = "MovieDetails"
    combined_string = sub1 + "+" + sub2
    subreddit = reddit.subreddit(combined_string)

    list = []
    for post in subreddit.search(movie, limit=1):
        post.comments.replace_more(limit=0)
        all_comments = post.comments.list()
        for comment in all_comments:
            list.append([comment.id, comment.submission.title, comment.body, comment.score, comment.created_utc])
    return list
