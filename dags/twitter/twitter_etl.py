# Import necessary libraries and modules
import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

# Define the ETL (Extract, Transform, Load) function
def run_twitter_etl():
    # Twitter API access keys and tokens
    access_key = ""  # Add your Twitter API access key
    access_secret = ""  # Add your Twitter API access secret
    consumer_key = ""  # Add your Twitter API consumer key
    consumer_secret = ""  # Add your Twitter API consumer secret

    # Twitter authentication
    auth = tweepy.OAuthHandler(access_key, access_secret)
    auth.set_access_token(consumer_key, consumer_secret)

    # Creating a Twitter API object
    api = tweepy.API(auth)

    # Fetch recent tweets from a specific user (e.g., '@elonmusk')
    tweets = api.user_timeline(screen_name='@elonmusk',
                               count=200,  # 200 is the maximum allowed count
                               include_rts=False,  # Exclude retweets
                               tweet_mode='extended'  # Necessary to keep full_text
                               )

    # List to store refined tweet data
    refined_tweets_list = []

    # Loop through each fetched tweet
    for tweet in tweets:
        # Extract relevant information from the tweet JSON
        text = tweet._json["full_text"]
        refined_tweet = {
            "user": tweet.user.screen_name,
            'text': text,
            'favorite_count': tweet.favorite_count,
            'retweet_count': tweet.retweet_count,
            'created_at': tweet.created_at
        }
        refined_tweets_list.append(refined_tweet)

    # Convert the list of refined tweets to a Pandas DataFrame
    df = pd.DataFrame(refined_tweets_list)

    # Save the DataFrame to a CSV file named 'refined_tweets.csv'
    df.to_csv('refined_tweets.csv')
