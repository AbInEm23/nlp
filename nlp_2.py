import pathlib
from textblob import TextBlob
import nltk
from pathlib import Path
import pandas as pd 


#nltk.download('stopwords')
from nltk.corpus import stopwords

stops = stopwords.words('english')
#print(stops)
blob = TextBlob("Today is a beautiful day.")
print(blob.words)

cleanlist = [word for word in blob.words if word not in stops]
print(cleanlist)

blob = TextBlob(Path('RomeoAndJuliet.txt').read_text())

print(blob.words.count('Joy'))
print(blob.word_counts["juliet"])

more_stops = ['thee','thy','thou']
stops += more_stops

items = blob.word_counts.items()
#print(items)

clean_items = [i for i in items if i[0] not in stops]
print(clean_items[:10])

from operator import itemgetter

#sorted_items = sorted(clean_items)

sorted_items = sorted(clean_items, key = itemgetter(1), reverse = True)
print(sorted_items[:10])

top20 = sorted_items[:20]
df = pd.DataFrame(top20, columns= ["word","count"])
print(df)
import matplotlib.pyplot as plt 
df.plot.bar(x="word",y="count",legend=False, color= ["y","c","m","b","g","r"])

plt.title("show boy")
plt.gcf().tight_layout()
plt.show()
