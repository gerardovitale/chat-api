import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import pandas as pd
from collect_comments import collect_comments
nltk.download("vader_lexicon")

SAVE_PATH = '../chat-api/output/sentiment_describe.csv'

def sentiment_analysis(translation=False):
    ig_comments = collect_comments()

    if translation == True:
        # trans_comments = [TextBlob(comment).translate(from_lang="es",to="en") for comment in ig_comments]
        for i in range(len(ig_comments)):
            try:
                ig_comments[i] = TextBlob(ig_comments[i]).translate(from_lang="es",to="en")
            except:
                continue

    sia = SentimentIntensityAnalyzer()
    punc = pd.DataFrame([sia.polarity_scores(_) for _ in ig_comments])
    describe = punc.describe()
    describe.to_csv(SAVE_PATH)

sentiment_analysis()