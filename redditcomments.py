import praw

reddit = praw.Reddit(client_id='kTtEDzfVknEtUQ',
                     client_secret='x',
                     username='prawtutorial',
                     password='cookies!!',
                     user_agent='prawtutorialv1')

subreddit = reddit.subreddit('python')

hot_python = subreddit.hot(limit=5)

for submission in hot_python:
    print(submission.title)
