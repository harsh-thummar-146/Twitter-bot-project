#final code

import time
import tweepy

consumer_key='jfIPOZPBMIyh3R1Cm0GMLeQC7'
consumer_secret='nvNv1VAF1vpZ7GIkHfNk3UPlgfbTLraiy3kDDPMgCH2hQ9GK5Z'
access_token='1400730890183995392-eXsqt6PMrZ36dBxXr0Ipo90pcU2CWT'
access_token_secret='V5uRIizBeY8getyomdQkIcM6UrLvsz0to78rDaxG5KKKw'

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


