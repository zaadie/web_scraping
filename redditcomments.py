import praw

reddit = praw.Reddit(client_it = 'kTtEDzfVknEtUQ',
                    client_secret = '6DAtdBN1HJbRnRZAxXvUikyaKKU',
                    username = 'prawtutorial',
                    password = 'cookies',
                    user_agent = 'prawtutorialv1')

subreddit = reddit.subreddit('python')

hot_python = subreddit.hot()