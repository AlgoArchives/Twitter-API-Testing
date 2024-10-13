import tweepy

# Replace these with your own credentials
api_key = 'your_api_key'
api_secret_key = 'your_api_secret_key'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
api = tweepy.API(auth)

# Post a tweet
api.update_status("Hello from Twitter API!")

# Get your timeline tweets
timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")