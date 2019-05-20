from TopicExtractor import TopicExtractor
import csv

te = TopicExtractor()
no_topics = 20

topics = te.getTopicWords(no_topics,10)

def toWords(l):
    ret = []
    for word in l:
        ret.append(str(word[0]).lower())
    return ret

def findCoOccurances(i,j):
    c = 0
    for wordi in i:
        if wordi in j:
            c+=1
    return c

counts = []
for i in range(len(topics)):
    counts.append([])
    for j in range(len(topics)):
        counts[i].append(0)

for i in range(len(topics)):
    topici = topics[i]
    for j in range(len(topics)):
        topicj = topics[j]
        counts[i][j] = findCoOccurances(toWords(topici),toWords(topicj))

csv_file = "../R/TopicOccurencesPerTestament2.csv"
with open(csv_file, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(counts)