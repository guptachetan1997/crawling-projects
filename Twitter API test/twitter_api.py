import twitter
import csv

oauth_object = []
file = open("oauth.datas", 'r')
for row in file:
	oauth_object.append(str(row))

file.close()

api = twitter.Api(consumer_key=oauth_object[0],
                      consumer_secret=oauth_object[1],
                      access_token_key=oauth_object[2],
                      access_token_secret=oauth_object[3])


tweets = api.GetSearch(term = "earthquake", count=10)
# print tweets
for tweet in tweets:
	print tweet.text
