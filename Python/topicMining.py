
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
print(tfidf_vect.get_feature_names())

nmf = NMF(n_components=10, random_state=1, alpha=.1,
          l1_ratio=.5, init='nndsvd').fit(tfidf)


def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic %d:" % (topic_idx))
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))


no_top_words = 10
display_topics(nmf, tfidf_vect.get_feature_names(), no_top_words)