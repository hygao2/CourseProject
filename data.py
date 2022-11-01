import praw
import pandas as pd

my_client_id = 'dkmj5CVNjnzx2esWgeViEg'
my_client_secret = '6Hh3UEdpqmXdMqi03sLYDhCSYJOYZA'
my_user_agent = 'cs410_movie_nlp'

reddit = praw.Reddit(client_id=my_client_id, client_secret=my_client_secret, user_agent=my_user_agent)

# extract initial reddit posts / comments for movie reviews
posts = []
ml_subreddit = reddit.subreddit('moviecritic')
for post in ml_subreddit.hot(limit=1000):
    posts.append([post.title, post.id, post.selftext, post.score, post.upvote_ratio, post.created])
print('finished posts')
comments = []
for post in posts:
    submission = reddit.submission(post[1])
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
        body = comment.body.replace('\u200b', '')
        comments.append([post[0], comment.id, body, comment.score, 0, comment.created_utc])
posts = posts + comments
print('finished comments')
df = pd.DataFrame(posts, columns=['title', 'id', 'body', 'score', 'upvote_ratio', 'created'])
df.to_csv('reddit_scraped_movie_comments.csv')
