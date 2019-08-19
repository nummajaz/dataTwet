import tweepy
from textblob import TextBlob


consumer_key = 'DURGkMYyFwRgaR1A1KjUJKscr'
consumer_secret = 'AMmslOruBgZjOUvPdI2gS8YTAk60KTImpuV191hNTmFB4Q9R9m'

acces_token = '1154352564344721408-a5h6wI0bzQ1uPxva3mfRRQbrTSYnz4'
acces_token_scret = 'hf56TQKn4nvoBbEVCVQPGwAQa09mHWllgvuT7GcHRvjns'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acces_token, acces_token_scret)

api = tweepy.API(auth)

public_tweets = api.search('jazuli')
for tweet in public_tweets:
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)