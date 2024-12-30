import tweepy
import os
from dotenv import load_dotenv
load_dotenv(verbose=True)
img ="image.png"
text = "안녕하세요 Tweepy 테스트 입니다2"

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
media_id= api.media_upload(filename=img).media_id_string
result = client.create_tweet(text=text,media_ids=[media_id])
