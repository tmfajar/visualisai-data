import tweepy
from textblob import TextBlob
from tweepy import OAuthHandler

import pandas as pd
import re
import time
import json

import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

        consumer_key = 'VAWGtDPbxEcMWPMzYEpjx22VF' 
        consumer_secret = 'I01IOPgqIyKlLvOPZyBQ7h0dq4fCHDytPoz9rAtdu8hlTZL1DU' 
        access_token = '864948672-6JbAzTt7OXyqLUcqHRWOq3yQXX6q7g7UQqcLdB8v'
        access_token_secret = 'n651dR2uGoYfDq6poeqE3xnvB68AO1THhDrCXtzAPEfTY'

# Membuat objek otentikasi
authenticate = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    
# Memasukkan kode akses token dan kode secret akses token
authenticate.set_access_token(access_token, access_token_secret) 
    
# Membuat objek API ketika melewatkan informasi otentifikasi
api = tweepy.API(authenticate, wait_on_rate_limit = True)

# Mengekstrak 200 twit terakhir dari user Twitter
posts = api.user_timeline(screen_name="lfc", count = 200, lang ="en", tweet_mode="extended")

# # Membuat dataframe dengan kolom bernama Tweets 
df = pd.DataFrame([tweet.full_text for tweet in posts], columns=['Tweets'])

# Membuat fungsi untuk membersihkan twit
def cleanTxt(text):
    text = re.sub('@[A-Za-z0–9]+', '', text) #Removing @mentions
    text = re.sub('#', '', text) # Removing '#' hash tag
    text = re.sub('RT[\s]+', '', text) # Removing RT
    text = re.sub('https?:\/\/\S+', '', text) # Removing hyperlink
    return text


# Proses membersihkan dataframe menggunakan fungsi cleanTxt
df['Tweets'] = df['Tweets'].apply(cleanTxt)


# Visualisasi Word Cloud
allWords = ' '.join([twts for twts in df['Tweets']])
wordCloud = WordCloud(colormap="gray", width=1600, height=800, random_state=30, max_font_size=200, min_font_size=20).generate(allWords)

# Menampilkan (Plotting) Word Cloud
plt.figure( figsize=(20,10), facecolor='k')
plt.imshow(wordCloud, interpolation="bilinear")
plt.axis('off')
plt.show()