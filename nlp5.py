from wordcloud import WordCloud
import imageio
import spacy
import textblob
from pathlib import Path
import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from textblob import TextBlob
stops = stopwords.words('english')


text = Path('book of John text.txt').read_text()

blob = TextBlob(text)

print(blob)
'''
df = pd.DataFrame(text, columns = ['word', 'count'])
print(df)

mask_image = imageio.imread('mask_circle.png')

wordcloud = WordCloud(colormap='prism', mask = mask_image, background_color='white')

wordcloud = wordcloud.generate(text)

wordcloud = wordcloud.to_file('BookOfJohnCircle.png')

print('done')
'''