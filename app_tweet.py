#final code

import time
import tweepy
import os


consumer_key=os.getenv('consumer_key')
consumer_secret=os.getenv('consumer_secret')
access_token=os.getenv('access_token')
access_token_secret=os.getenv('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
print('Authentication approved')
while True:
  user=api.get_user('@harsh14559937')
  u=user.friends_count
  api.update_profile(name=f'Harsh {u} following')
  print(f'Harsh {u} following')


  time.sleep(60)

## it is running in while loop so that it can update result as the followers changes


