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