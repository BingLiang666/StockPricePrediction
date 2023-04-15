# StockPricePrediction
This is a repo for the course project of "CS663 Machine Learning"

### MSFT.csv
This file contains all the stock data of Microsoft.

The Date is from 2022-12-01 to 2023-03-17. (2023-03-18 and 2023-03-19 are weekends).

### output.csv.zip
This file is the output file of sentiment analysis using roBERTa.

The roBERTa language model is utilized to perform sentiment analysis on Twitter data, generating the 'Negative', 'Neutral', and 'Positive' columns with associated values. 

A new 'Sentiment' column is derived based on a scoring system, with

 - -1 indicating negative sentiment
 
 - 0 indicating neutral sentiment, and 
 
 - 1 indicating positive sentiment

For more details, you can check the "Sentiment_Analysis_roBERTa.ipynb" in branch shumin_new.