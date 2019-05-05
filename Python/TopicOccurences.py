from TopicExtractor import TopicExtractor
import numpy as np
import string

TE = TopicExtractor()

books = TE.books

topics = TE.getTopicWords(10, 10)

tmpTopics = []

for topic in topics:
    for tupel in topic:
        tmpTopics.append(tupel[0])

tmpTopics = np.array(tmpTopics)
tmpTopics = np.unique(tmpTopics)

print(tmpTopics)

bookDictionaries = []

for book in books:
    dictionary = dict((item, 0) for item in tmpTopics)

    for chapter in book:

        for text in chapter:

            for s in text.split(' '):
                tmp = s.translate(str.maketrans('', '', string.punctuation))
                if tmp in dictionary:
                    dictionary[tmp] += 1

    bookDictionaries.append(dictionary)


print(bookDictionaries)
