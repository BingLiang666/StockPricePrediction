# StockPricePrediction
This is a repo for the course project of "CS663 Machine Learning"

### retrieve_chatgpt_tweets.py
Thie file contains python codes that retrieve tweets from Twitter using snscrape.

### chatgpt_tweets.csv.zip
This file contains 305,464 tweets containing keyword "chatgpt" from 12/1/2022 to 3/19/2023.

### MSFT.csv
This file contains all the stock data of Microsoft.

The Date is from 2022-12-01 to 2023-03-20.

### output.csv.zip
This file is the output file of sentiment analysis using roBERTa.

The roBERTa language model is utilized to perform sentiment analysis on Twitter data, generating the 'Negative', 'Neutral', and 'Positive' columns with associated values. 

A new 'Sentiment' column is derived based on a scoring system, with

 - -1 indicating negative sentiment
 
 - 0 indicating neutral sentiment, and 
 
 - 1 indicating positive sentiment

For more details, you can check the "Sentiment_Analysis_roBERTa.ipynb" in branch shumin.

### assign_stock_price_for_each_tweet.ipynb
This file contains python codes that assign each tweet a stock price which is on the closest available day, such as assigning tweets posted on 12/24, 12/25, and 12/26 the stock price of 12/27.

### merged_tweets_and_stock_prices.csv.zip
This file contains the tweets and the stock price associated to each tweet.

### ML Project - RNN.ipynb
This file contains python codes that train model and use this model to make prediction.
