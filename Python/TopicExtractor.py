import numpy as np
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import xml.etree.ElementTree as ET
import pandas as pd


from gensim.corpora.dictionary import Dictionary
from gensim.models.nmf import Nmf
from gensim.models.ldamodel import LdaModel
import spacy
from spacy.lang.en import English
parser = English

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
                    text = []
                    for word in verse.text.split(' '):
                        w = self.lemmatizer.lemmatize(word.lower())
                        if w not in self.stopWords and w not in self.manualStopWords:
                            text.append(w)
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
                    v.append(verse.text)              
                b.append(v)
            books.append(b)

        return books

    def getTopicWords(self, no_components, no_words):
        common_dictionary = Dictionary(self.bible)
        common_corpus = [common_dictionary.doc2bow(text) for text in self.bible]
        model = Nmf(common_corpus,num_topics=no_components, random_state=1, id2word=common_dictionary)

        df = []
        word_dict = {}
        for i in range(no_components):
            words = model.show_topic(i, topn = no_words)
            word_dict['Topic # ' + '{:02d}'.format(i+1)] = [i[0] for i in words]
        df = pd.DataFrame(word_dict)
        return df

    def getTopicWordsLDA(self, no_components, no_words):
        common_dictionary = Dictionary(self.bible)
        common_corpus = [common_dictionary.doc2bow(text) for text in self.bible]
        model = LdaModel(common_corpus,num_topics=no_components, random_state=1, id2word=common_dictionary)

        df = []
        word_dict = {}
        for i in range(no_components):
            words = model.show_topic(i, topn = no_words)
            word_dict['Topic # ' + '{:02d}'.format(i+1)] = [i[0] for i in words]
        df = pd.DataFrame(word_dict)
        return df

t = TopicExtractor()

print(t.getTopicWords(10,10))
print(t.getTopicWordsLDA(10,10))