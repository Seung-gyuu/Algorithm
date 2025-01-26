import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    #to find the IDs of the invalid tweets
    #invalid if the number of characters used in the content is strictly greater than 15.
    tweets["content"] = tweets["content"].str.len()
    tweets = tweets[tweets["content"] > 15 ][["tweet_id"]]
    return tweets
