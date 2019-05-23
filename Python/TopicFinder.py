from TopicExtractor import TopicExtractor
import csv

te = TopicExtractor()

topics = te.getTopicWords(20,10)

csv_file = "../R/TopicNaming.csv"
with open(csv_file, 'w') as csvfile:
    writer = csv.writer(csvfile)
    for topic in topics:
        t = []
        for word, measure in topic:
            t.append(word)
        writer.writerow(t)