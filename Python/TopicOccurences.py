from TopicExtractor import TopicExtractor
import csv
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
bookCounter = 1990

for book in books:
    dictionary = dict((item, 0) for item in tmpTopics)
    dictionary['timeOfBook'] = bookCounter
    bookCounter += 1

    for chapter in book:

        for text in chapter:

            for s in text.split(' '):
                tmp = s.translate(str.maketrans('', '', string.punctuation))
                if tmp in dictionary:
                    dictionary[tmp] += 1

    bookDictionaries.append(dictionary)


print(bookDictionaries)
tmpTopics = np.append(tmpTopics, 'timeOfBook')
csv_columns = ['word', 'value', 'year']

csv_file = "../R/TopicOccurencesPerBook.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in bookDictionaries:
            timeOfBook = data['timeOfBook']
            for item in data:
                if not item == 'timeOfBook':
                    dicti = {'word': item, 'value': data[item], 'year': timeOfBook}
                    writer.writerow(dicti)

except IOError:
    print("I/O error")
