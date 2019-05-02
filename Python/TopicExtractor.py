
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
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
    book_names = []

    stopWords = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    manualStopWords = []

    def __init__(self):
        self.readBible()

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
            self.book_names.append(book.attrib['n'])

        whole_bible = []
        for book in books:
            for chapter in book:
                for verse in chapter:
                    whole_bible.append(verse)

        self.bible = whole_bible
        self.books = books

    def getFullTextBooks(self):
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
                        text += word
                    v.append(text)              
                b.append(v)
            books.append(b)

        whole_bible = []
        for book in books:
            for chapter in book:
                for verse in chapter:
                    whole_bible.append(verse)
            
        return whole_bible

    def getTopicWords(self, no_components, no_words):
        tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')
        tfidf = tfidf_vectorizer.fit_transform(self.bible)
        tfidf_feature_names = tfidf_vectorizer.get_feature_names()

        model = NMF(n_components=no_components, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)

        allTopicWords = []

        for topic_idx, topic in enumerate(model.components_):
            print ("Topic %d:" % (topic_idx))
            print (" ".join([tfidf_feature_names[i]
                for i in topic.argsort()[:-no_words - 1:-1]]))
        
        return allTopicWords


t = TopicExtractor()
t.getTopicWords(10,20)