from wordcloud import WordCloud
import imageio
import textblob
from pathlib import Path
import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from textblob import TextBlob

stops = stopwords.words('english') 

additional =['thy', 'ye', 'verily', 'thee', 'hath', 
'say', 'thou', 'art', 'shall']


stops += additional

text = Path('book of John text.txt').read_text()


blob = TextBlob(text)

#print(blob)

from operator import itemgetter

items = blob.noun_phrases

items = [item for item in items if item[0] not in stops]

sorted_items = sorted(items, key = itemgetter(1), reverse = True)

top15 =sorted_items[1:16]

df = pd.DataFrame(top15, columns=['word', 'count'])

mask_image = imageio.imread('mask_circle.png')

wordcloud = WordCloud(colormap='prism', mask = mask_image, background_color='white')
print(df)
'''
wordcloud = wordcloud.generate(text)

wordcloud = wordcloud.to_file('BookOfJohnCircle.png')

print('done')
'''