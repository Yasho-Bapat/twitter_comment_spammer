import tweepy

auth = tweepy.OAuthHandler('GROacRrJYa78eeX2ZuJNofuIH', 'UzFd6hcbYwKKNSicu1kt8KhyhoCFV3yPMGuhX4j5pgCzvNXL3u')
auth.set_access_token('1242846079776722945-crFCmDmOV00gxW7l0c5EnmeBE9lzNB', 'iONwOIvsbqYTJmkQBbm52eiYEDFlyLXdGxh3RdbuDQqAD')

api = tweepy.API(auth, wait_on_rate_limit=True)

user = input("enter user: ")
comment = input("enter comment phrase: ")
target_tweets = api.user_timeline(screen_name = user, count = 50)
for tweet in target_tweets:
    print(tweet.text)
    api.update_status(status = ("@" + tweet.user.screen_name + " " + comment), in_reply_to_status_id = tweet.id)