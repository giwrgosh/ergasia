import tweepy
from tweepy import OAuthHandler
import json
 
 
 
user= input ("Πληκτρολογήστε το όνομα του προφιλ του χρήστη που θέλετε να μάθετε την δημοφιλέστερη λέξη των 10 τελευτέων tweets τους:") 

 

 

consumer_key = 'T4QAW1Me7DJAumZ6snx1yJX2q'
consumer_secret = 'pvEb9MKpjkPZq2TV2tCYKLOFQCU0Sopr8dcqt7yKminO0BGbfL'
access_token = '962272370886107136-TwPMggJ0B8o061RZhgvd9hRqBuQWzMI'
access_secret = 'g9lVLBlzE6IMkMRVIqkJ9pINqGXJZrT9AbU1EBdW4Ss93'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
with open('mytweets.json', 'r') as f:
	results = twitter.statuses.user_timeline(screen_name = user)
	terms_all = [term for term in preprocess(tweet['text'])]
	count_all.update(terms_all)
	line = f.readline(10)
	tweet = json.loads(line)
	print(count_all.most_common(10))