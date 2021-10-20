from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

#print(blob.sentences)

#print(blob.words)

#print(blob.tags)

#print(blob.noun_phrases)

#print(round(blob.sentiment.polarity, 3))
#print(round(blob.sentiment.subjectivity, 3))


#do it by sentences
#for sentence in blob.sentences:
    #print(sentence)
    #print(round(sentence.sentiment.polarity, 3))


from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

#print(blob.sentiment)

#for sentence in blob.sentences:
    #print(sentence.sentiment)


spanish = blob.translate(to = 'es')
#print(spanish)


chineses = blob.translate(to = 'zh')
#print(chineses)


#translates back to ENG
#print(chineses.translate())

from textblob import Word

index = Word('index)')

print(index.pluralize())

cacti = Word('cacti')
print(cacti.singularize())

#wordlist
animals = TextBlob('dog cat fish bird').words
print(animals.pluralize())

#spellcheck and correction
word = Word('theyr')

print(word.spellcheck())

print(word.correct())

#Normalization (of words)

word1 = Word('Studies')

word2 = Word('Varieites')

print(word1.stem())
print(word2.stem())

print(word1.lemmatize())
print(word2.lemmatize())

#Definitions, Synonms, and Antonyms
happy = Word('happy')

print(happy.definitions)

print(happy.synsets)

for s in happy.synsets:
    for l in s.lemmas():
        print(l.name())

synonym = happy.synsets[1].lemmas()[0].name()
print(synonym)

antonym = happy.synset[0].lemmas()[0].name()
print(antonym)