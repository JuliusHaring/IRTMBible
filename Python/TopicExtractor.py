
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import numpy as np
from nltk.stem.snowball import EnglishStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk
import re
import os
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

class TopicExtractor:
    topicWords = []
    bible = []
    books = []

    stopWords = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    manualStopWords = ["god", "lord"]

    def __init__(self, no_components, no_words):
        self.readBible()
        self.getTopicWords(no_components, no_words)

    def readBible(self):
        raw = ET.parse('NIV.xml')
        root = raw.getroot()
        books = []

        for book in root.getchildren():
            b = []
            for chapter in book.getchildren():
                v = []
                for verse in chapter.getchildren():
                    text = ''
                    for word in verse.text.split(' '):
                        w = self.lemmatizer.lemmatize(word.lower())
                        if w not in self.stopWords and w not in self.manualStopWords:
                            text += w +' '
                    v.append(text)

                b.append(v)
            books.append(b)

        whole_bible = []
        for book in books:
            for chapter in book:
                for verse in chapter:
                    whole_bible.append(verse)

        self.bible = whole_bible
        self.books = books

        

    def getTopicWords(self, no_components, no_words):
        c_vect = CountVectorizer()
        counts = c_vect.fit_transform(self.bible)

        model = LatentDirichletAllocation(n_components=no_components, random_state=1).fit(counts)

        allTopicWords = []

        for _, topic in enumerate(model.components_):
            allTopicWords.append(" ".join([c_vect.get_feature_names()[i]
                                    for i in topic.argsort()[:-no_words - 1:-1]]).split())

        self.topicWords = allTopicWords

t = TopicExtractor(15,10)

for line in t.topicWords:
    print(line)