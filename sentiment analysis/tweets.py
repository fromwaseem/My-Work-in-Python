# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '521627718-ebD5GtJqozNn2hnDEOXvMqGAw8ouBhNgj8hVeJBr'
ACCESS_SECRET = 'xWEVueaWi5RSZyHUNzArwSxutx8U6U4wF13J0s4mnF5k7'
CONSUMER_KEY = 'wNS5zKYMQJyIrEiyKZscu0hgy'
CONSUMER_SECRET = 'HCFUwVavMyhDCOlsDYlpByzrAKg8JzVAmER1ZlqXX38qyGdXqU'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 1000
for tweet in iterator:
	tweet_count -= 1
	# Twitter Python Tool wraps the data returned by Twitter 
	# as a TwitterDictResponse object.
	# We convert it back to the JSON format to print/score
	data=json.dumps(tweet, indent=4)
	print(data)

	# The command below will do pretty printing for JSON data, try it out
	# print json.dumps(tweet, indent=4)
	   
	if tweet_count <= 0:
		break 
	f=open("output.txt",'w')
	f.write(data)
	 # f.close()
