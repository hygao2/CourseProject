import praw
import pandas as pd

client_id = "dYNuyLuHfhJZ0apmTw7Pkw"
client_secret ="qt-8J7eEjzcEg-Mx9Hwrq00iFgSpeg"
user_agent = "web:com.example.sentimentanalysis:v1.0.0",


reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

#returns list of comments related to movie, from subreddit(s) and movie chosen by user 

def movie_comments(movie, subreddit, limit):
    list = []
    for post in subreddit.search(movie, limit=limit):
        post.comments.replace_more(limit=0)
        all_comments = post.comments.list()
        for comment in all_comments:
            list.append([comment.id, comment.submission.title, comment.body, comment.score])
    return list
    
sub1 = "movies"
sub2 = "MovieDetails"
combined_string = sub1 + "+" + sub2
combined_sub = reddit.subreddit(combined_string)


movie = "The Dark Knight"
limit = 10 

comments = movie_comments(movie,combined_sub,limit)
df = pd.DataFrame(comments, columns=['id', 'post title', 'body', 'score'])
df
