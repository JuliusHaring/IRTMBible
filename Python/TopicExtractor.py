
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
from sklearn.cluster import KMeans
import numpy as np
from nltk.stem.snowball import EnglishStemmer
from nltk.corpus import stopwords
import nltk
import re
import os
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

class TopicExtractor:
    topicWords = []

    def __init__(self, no_components, no_words):
        self.getTopicWords(no_components, no_words)

    def getTopicWords(self, no_components, no_words):
        stopWords = set(stopwords.words('english'))


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
                        w = word.lower()
                        if w not in stopWords:
                            text += w+' '
                    v.append(text)

                b.append(v)
            books.append(b)

        whole_bible = []
        for book in books:
            for chapter in book:
                for verse in chapter:
                    whole_bible.append(verse)


        tfidf_vect = TfidfVectorizer()
        tfidf = tfidf_vect.fit_transform(whole_bible)

        nmf = NMF(n_components=no_components, random_state=1, alpha=.1,
                l1_ratio=.5, init='nndsvd').fit(tfidf)

        allTopicWords = []

        for topic_idx, topic in enumerate(nmf.components_):
            allTopicWords.append(" ".join([tfidf_vect.get_feature_names()[i]
                                    for i in topic.argsort()[:-no_words - 1:-1]]).split())

        self.topicWords = allTopicWords

t = TopicExtractor(10,20)

for line in t.topicWords:
    print(line)