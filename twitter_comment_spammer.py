import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

user = input("enter user: ")
comment = input("enter comment phrase: ")

target_tweets = api.user_timeline(screen_name = user, count = 50)

for tweet in target_tweets:
    print(tweet.text)
    api.update_status(status = ("@" + tweet.user.screen_name + " " + comment), in_reply_to_status_id = tweet.id)
