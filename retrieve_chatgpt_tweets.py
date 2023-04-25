# Retrieve tweets from Twitter that contain keyword "chatgpt" from certain start date and end date
# Revieve certain amount of tweets each time. (10,000 in this case)

import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "chatgpt lang:en until:2022-12-3 since:2022-12-1 -filter:links -filter:replies"
tweets = []
limit = 10000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)

# save to csv
df.to_csv('tweets_12.2.csv')