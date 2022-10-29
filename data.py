import praw
import pandas as pd

my_client_id = 'dkmj5CVNjnzx2esWgeViEg'
my_client_secret = '6Hh3UEdpqmXdMqi03sLYDhCSYJOYZA'
my_user_agent = 'cs410_movie_nlp'

reddit = praw.Reddit(client_id=my_client_id, client_secret=my_client_secret, user_agent=my_user_agent)

#extract inital reddit posts / comments for movie reviews
posts = []
ml_subreddit = reddit.subreddit('moviecritic')
for post in ml_subreddit.hot(limit = 1000):
    post.upvote
    text = []
    text.append(post.selftext)
    submission = reddit.submission(id=post.id)
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
        text.append(comment)
    
    posts.append([post.title, post.id, text, post.score, post.upvote_ratio, post.created])
df = pd.DataFrame(posts,columns=['title', 'id', 'body', 'score', 'upvote_ratio', 'created'])
df.to_csv('reddit_scraped_movie_comments.csv')
