# markets-and-the-media

Can we predict future market trends based on news media sentiment?
Market trends will be extracted using the YFinance API.
News media sentiment will be extracted from the NYTimes using the NYTimes API (or possibly the Financial Times depending on availability).
Sentiment analysis will be done using natural language processing (via either TextBlob or NLTK).
We will visualize the relationship between a metric of sentiment analysis vs stock price at time $t - t_{article\,published}$, for articles purportedly related to the stock (likely via word match).
Following visualization, we will train a ML regression model to the data.

This project was built during the Erdos Institute Data Science Boot Camp, Spring 2023.
