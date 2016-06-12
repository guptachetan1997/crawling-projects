import twitter
import csv

oauth_object = ["", "", "", ""]
file = open("oauth.datas", 'r')
for row,i in zip(file,range(0,4)):
    oauth_object[i] = row[:len(row)-1]

file.close()

# oauth_object[0] = '5AVMLWLoq0vMWMwaOi80PRzLR'
# oauth_object[1] = 'hjDs8amMcyWBCQhIQX9kWPJ6TfjVXKSCzg6GNZIKr1QpCxCEd4'
# oauth_object[2] = '384641534-EiZ0Snu1fJdtTs4qe1COc2MloZvZ1G5houEIdsVr'
# oauth_object[3] = '79Qrfx504I5bLgyE9S4drZDG6m80djYb0vqAQuChB5rpW'

api = twitter.Api(consumer_key=oauth_object[0],
                      consumer_secret=oauth_object[1],
                      access_token_key=oauth_object[2],
                      access_token_secret=oauth_object[3])

# print(api.VerifyCredentials())
tweets = api.GetSearch(term="AAP", count=10, lang="en")
for tweet in tweets:
	print (tweet.text).encode('utf8')

