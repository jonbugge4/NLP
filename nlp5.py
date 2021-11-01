from wordcloud import WordCloud
import imageio
import textblob
from pathlib import Path
import pandas as pd
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from textblob import TextBlob

stops = stopwords.words('english') 

additional =['thy', 'ye', 'verily', 'thee', 'hath', 
'say', 'thou', 'art', 'shall']


stops += additional

text = Path('book of John text.txt').read_text()


blob = TextBlob(text)

noun = blob.noun_phrases
#print(blob)

from operator import itemgetter

items = blob.word_counts.items()

cleaned_items = [item for item in items if item[0] not in stops if item[0] in noun]


sorted_items = sorted(cleaned_items, key = itemgetter(1), reverse = True)

top15 =sorted_items[0:15]
print(top15)

wordcloud = WordCloud(colormap='Blues', background_color='grey')

text = ''
for x in top15:
    print(x)
    text += x[0] + ' '

wordcloud = wordcloud.generate(text)
wordcloud = wordcloud.to_file('BookOfJohnCircle.png')

print('done')
