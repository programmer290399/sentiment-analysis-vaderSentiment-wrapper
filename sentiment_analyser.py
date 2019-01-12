from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


sentence = input('Enter the senntence for analysis :')

analyzer = SentimentIntensityAnalyzer()
sentiment = analyzer.polarity_scores(sentence)

if sentiment['compound'] >= 0.05:
    sentence_category = 'Positive'
elif -0.05 <= sentiment['compound'] < 0.05:
    sentence_category = 'Neutral'
else:
    sentence_category = 'Negative'

sentence_data = dict()

print('This sentence is:', sentence_category)
print (dict(sentiment))