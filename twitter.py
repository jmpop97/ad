import tweepy
import os
from dotenv import load_dotenv
load_dotenv(verbose=True)
imgPath ="image.png"
textPath = "text.txt"
with open(textPath, "r") as f:
    text = f.read()

print(text)


consumer_key=os.environ['CONSUMER_KEY']
consumer_secret=os.environ['CONSUMER_SECRET']
access_token=os.environ['ACCESS_TOKEN']
access_token_secret=os.environ['ACCESS_TOKEN_SECRET']
bearer_token=os.environ['BEARER_TOKEN']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)



client = tweepy.Client(
    consumer_key=os.environ['CONSUMER_KEY'],
    consumer_secret=os.environ['CONSUMER_SECRET'],
    access_token=os.environ['ACCESS_TOKEN'],
    access_token_secret=os.environ['ACCESS_TOKEN_SECRET'],
    bearer_token=os.environ['BEARER_TOKEN']
)
media_id= api.media_upload(filename=imgPath).media_id_string
result = client.create_tweet(text=text,media_ids=[media_id])
