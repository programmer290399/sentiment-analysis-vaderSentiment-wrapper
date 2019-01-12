# Sentiment-analyser-vaderSentiment-wrapper
Just enter any statement in English and predict its sentiments   


## Steps to setup this project :
* Run command `pip install -r requirements.txt`
* Run `sentiment_analyser.py` to analyze any statement 

## Giving Score to a sentence 

Compound score of the sentiment can be treated as a useful metric when you want single unidimensional measure of the sentiment.

The positive, neutral and negative scores are ratios for proportions of text that fall in each category (so these should all add up to be 10... or close to it with float operation). These are the most useful metrics if you want multidimensional measures of sentiment for a given sentence.

Threshold has been places as per their documentation, however you can tune as per your wish in the code.
