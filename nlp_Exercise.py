import pathlib
from textblob import TextBlob
import nltk

from pathlib import Path
import pandas as pd 
from operator import itemgetter
from nltk.corpus import stopwords

from os import path
from pathlib import Path
import imageio
from wordcloud import WordCloud

stops = stopwords.words('english')
additional_words = ['thy', 'ye', 'verily', 'thee', 'hath', 'say', 'thou', 'art', 'shall',"'"]
stops += additional_words

#print(stops)

blob = TextBlob(Path("book of John text.txt").read_text())
nouns = blob.noun_phrases
#print(nouns)


items = blob.word_counts.items()
clean = [word for word in items if word[0] not in stops]
clean_nouns = [noun for noun in clean if noun[0] in nouns]
sorted_list = sorted(clean_nouns, key= itemgetter(1), reverse= True) 
#clean_nouns_list = [i[0] for i in sorted_list]
top15 = str(sorted_list[:15])

print(top15)

mask_image = imageio.imread('mask_oval.png')
wordcloud = WordCloud(colormap= 'prism', mask = mask_image, background_color = 'white')
wordcloud = wordcloud.generate((top15).replace("'",''))
wordcloud = wordcloud.to_file('BookofJohnOval.png')
print("done out here")
