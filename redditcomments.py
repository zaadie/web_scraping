import praw

reddit = praw.Reddit(client_id='kTtEDzfVknEtUQ',
                     client_secret='6DAtdBN1HJbRnRZAxXvUikyaKKU',
                     username='CyberZii',
                     password='Sha25694!!',
                     user_agent='prawtutorialv1')

subreddit = reddit.subreddit('python')
subreddit = reddit.subreddit('programmerhumor')

hot_python = subreddit.hot(programmerhumor=5)
top_progammerhumor = subreddit.top(limit=5)

# for submission in hot_python:
#     print(submission.title)

for submission in top_programmerhumor:
    print(submission.title)