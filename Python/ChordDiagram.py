from TopicExtractor import TopicExtractor
import pandas as pd
import csv

te = TopicExtractor()
no_topics = 20

books = te.getFullTextBooks()
topics = te.getTopicWords(no_topics,10)

testaments = ["",""]

for i in range(len(books)):
    book = books[i]
    for chapter in book:
        for sentence in chapter:
            if(i < 39):
                testaments[0] += sentence
            else:
                testaments[1] += sentence

counts = [[],[]]

def countWord(word,text):
    words = str(text).lower().split(" ")
    return words.count(str(word).lower())

def countTopic(topic, text):
    c = 0
    for word in topic:
        c+= countWord(word[0],text)
    return c

for i in range(len(topics)):
    counts[0].append(countTopic(topics[i],testaments[0]))
    counts[1].append(countTopic(topics[i],testaments[1]))

csv_file = "../R/TopicOccurencesPerTestament.csv"
with open(csv_file, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(counts)