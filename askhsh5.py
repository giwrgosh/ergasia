import tweepy
from tweepy import OAuthHandler
import json
 
 
 
user= input ("Πληκτρολογήστε το όνομα του προφιλ του χρήστη που θέλετε να μάθετε την δημοφιλέστερη λέξη των 10 τελευτέων tweets τους:") 

 

 


 
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