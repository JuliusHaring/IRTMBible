from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import numpy as np
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import xml.etree.ElementTree as ET

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
                    v.append(verse.text)              
                b.append(v)
            books.append(b)

        return books

    def getTopicWords(self, no_components, no_words):
        tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')
        tfidf = tfidf_vectorizer.fit_transform(self.bible)
        tfidf_feature_names = tfidf_vectorizer.get_feature_names()

        model = NMF(n_components=no_components, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)

        allTopicWords = []

        for topic_idx, topic in enumerate(model.components_):
            topicWords = [tfidf_feature_names[i] for i in topic.argsort()[:-no_words - 1:-1]]

            topicWordsScores = []

            for word in topicWords:
                wordScore = topic[np.where(np.array(tfidf_feature_names)==word)][0]
                topicWordsScores.append((word, wordScore))


            allTopicWords.append(topicWordsScores)
        
        return allTopicWords


    def getRawNMF(self,no_components):
        tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')
        tfidf = tfidf_vectorizer.fit_transform(self.bible)
        tfidf_feature_names = tfidf_vectorizer.get_feature_names()

        return = NMF(n_components=no_components, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)

t = TopicExtractor()
#print(t.getTopicWords(10,10))
# Access List 0, Item 0, TuppleItem 0 (name)
#print(t.getTopicWords(10,10)[0][0][0])