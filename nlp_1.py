from textblob import TextBlob
#import nltk
#nltk.download()

text = " i love you. but i hate you"

#blob = TextBlob(text)

#print(blob.sentences)
#print(blob.words)

#print(blob.tags)
#print(blob.noun_phrases)

#print(blob.sentiment)

#print(round(blob.sentiment.subjectivity), 3)
#print(round(blob.sentiment.subjectivity, 3))

'''
sentences = blob.sentences

for sentence in sentences:
    print(sentence)
    print(sentence.sentiment.polarity)




from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer= NaiveBayesAnalyzer())
#print(blob.sentiment)

for sentence in blob.sentences:
    print(sentence.sentiment)

spanish = blob.translate(to= 'es')
chinese = blob.translate(to= 'zh')

print(spanish)
print(spanish.translate)

print(chinese)
print(chinese.translate)


from textblob import Word

index = Word('index')
print(index.pluralize())

cacti = Word('cacti')
print(cacti.singularize())

animals = TextBlob('dog cat sun')
#print(animals.pluralize)

word = Word('theyr')
print(word.spellcheck())
print(word.correct())

word1 = Word('studies')
word2 = Word('varieties')

print(word1.stem())
print(word2.stem())

print(word1.lemmatize())
print(word2.lemmatize())

#Definitions, synonyms and Antonyms 

happy = Word('happy')
#print(happy.definitions)

tennyson = Word('tennyson')
#print(tennyson.definitions)

print(happy.synsets)
for s in happy.synsets:
    for lemma in s.lemmas():
        print(lemma.name())
'''
from textblob import Word
happy = Word('happy')

synonym = happy.synsets[1].lemmas()[0].name()
print(synonym)

