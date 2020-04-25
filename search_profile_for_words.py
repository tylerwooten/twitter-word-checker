import twitter
from secret import Secret
# limited to 3200 most recent tweets

badwords = ['fuck', 'shit']
user = '@ItsTylerWooten'  # can have @ or not - doesn't matter

api = twitter.Api(consumer_key=Secret.ckey,
                  consumer_secret=Secret.csecret,
                  access_token_key=Secret.atoken,
                  access_token_secret=Secret.asecret)
Since_id = 500
Max_id = 700
statuses = api.GetUserTimeline(screen_name=user, since_id=Since_id, count=100)  # count can go up to 200
posts = [s.text for s in statuses]
print(posts)
print('number of tweets:') #should be 1024 for me
print(len(posts))


bad_tweets = []
for item in posts:
    for word in badwords:
        if word in item:
            bad_tweets.append(item)


if len(bad_tweets) > 0:
    print('Found a bad one:')
    print(bad_tweets)
else:
    print('all clear :)')

