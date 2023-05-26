#!/usr/bin/env python
# coding: utf-8

# In[28]:


#Using TextBlob
from textblob import TextBlob

headlines = [
    "Google’s parent company reported earnings that were below analysts’ expectations",
    "Economic uncertainty weighs heavily on investor sentiment",
    "Company XYZ announces layoffs, leading to negative market reaction",
    "New government policies boost investor confidence",
]

# Perform sentiment analysis
for headline in headlines:
    blob = TextBlob(headline)
    sentiment = blob.sentiment
    polarity = sentiment.polarity
    subjectivity = sentiment.subjectivity

    print(f"Polarity: {polarity}")
    print(f"Subjectivity: {subjectivity}")
    print()


# In[29]:


#Using NLTK Sentiment Intensity Analyzer
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Create an instance of the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Sample text for sentiment analysis
headlines = [
    "Google’s parent company reported earnings that were below analysts’ expectations",
    "Economic uncertainty weighs heavily on investor sentiment",
    "Company XYZ announces layoffs, leading to negative market reaction",
    "New government policies boost investor confidence",
]

for headline in headlines:
    # Perform sentiment analysis
    sentiment_scores = sia.polarity_scores(headline)

    # Print the sentiment scores and label
    print("Sentiment Scores:", sentiment_scores)
    print()


# In[30]:


#Using VaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Sample news headlines
headlines = [
    "Google’s parent company reported earnings that were below analysts’ expectations",
    "Economic uncertainty weighs heavily on investor sentiment",
    "Company XYZ announces layoffs, leading to negative market reaction",
    "New government policies boost investor confidence",
]

# Perform sentiment analysis on each headline
for headline in headlines:
    sentiment_scores = analyzer.polarity_scores(headline)
    print(f"Headline: {headline}")
    print(f"Sentiment scores: {sentiment_scores}")
    print("---")


# In[31]:


#Using Pattern
from pattern.en import sentiment

headlines = [
    "Google’s parent company reported earnings that were below analysts’ expectations",
    "Economic uncertainty weighs heavily on investor sentiment",
    "Company XYZ announces layoffs, leading to negative market reaction",
    "New government policies boost investor confidence",
]

for headline in headlines:
    # Perform sentiment analysis
    polarity, subjectivity = sentiment(headline)


    # Print the sentiment analysis results
    print("Polarity Score: ", polarity)
    print("Subjectivity Score: ", subjectivity)
    print()

