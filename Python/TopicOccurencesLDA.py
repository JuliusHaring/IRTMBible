from TopicExtractor import TopicExtractor
import csv
import numpy as np
import string

TE = TopicExtractor()

books = TE.books

topics = TE.getTopicWordsLDA(20, 10)

tmpTopics = []

test = []
topicCounter = 0

for topic in topics:
    tmp = []
    #print(topic)
    for tupel in topic:
        tmpTopics.append(tupel[0])
        tmp.append(tupel[0])
    test.append(tmp)
    topicCounter += 1

print(test)

tmpTopics = np.array(tmpTopics)
tmpTopics = np.unique(tmpTopics)

print(tmpTopics)

bookDictionaries = []
bookCounter = 1000

testDict = []
testDictCounter = 0
c = 0
ct = 0

for book in books:
    bookname = 'book' + str(c)
    tmp = {'book' + str(c): []}
    ct = 0
    for item in test:
        tmp[bookname].append({'topic' + str(ct) : 0})
        ct += 1
    testDict.append(tmp)
    c += 1

print(testDict)
print(testDict[0])
c = 0

for book in books:
    #dictionary = dict((item, 0) for item in testDict[testDictCounter])
    #print(dictionary)
    #dictionary['timeOfBook'] = bookCounter
    #testDict['timeOfBook'] = bookCounter
    testDict[testDictCounter]['timeOfBook'] = bookCounter
    bookCounter += 1

    for chapter in book:

        for text in chapter:

            for s in text.split(' '):
                tmp = s.translate(str.maketrans('', '', string.punctuation))
                c = 0
                for arr in test:
                    if tmp in arr:
                        testDict[testDictCounter]['book' + str(testDictCounter)][c]['topic' + str(c)] += 1
                        #print(testDict[testDictCounter]['book' + str(testDictCounter)][c]['topic' + str(c)])
                        #testDict[bookCounter][str(c)] += 1
                        #print('book' + str(c))
                        #testDict[bookCounter]
                    c += 1
    testDictCounter += 1
    #bookDictionaries.append(dictionary)

print(testDict)

print(bookDictionaries)
tmpTopics = np.append(tmpTopics, 'timeOfBook')
csv_columns = ['topic', 'value', 'year']
c = 0
csv_file = "../R/TopicOccurencesPerBook.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in testDict:
            timeOfBook = data['timeOfBook']
            print(timeOfBook)
            for item in data['book' + str(c)]:
                #print(item)
                for t in item:
                    #print(item[t])
                    dicti = {'topic': t, 'value': item[t], 'year': timeOfBook}
                    writer.writerow(dicti)
                #if not item == 'timeOfBook':
                 #   dicti = {'word': item, 'value': data[item], 'year': timeOfBook}
                  #  writer.writerow(dicti)
            c += 1

except IOError:
    print("I/O error")
