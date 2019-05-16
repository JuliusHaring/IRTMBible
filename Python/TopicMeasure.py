from sklearn.metrics.cluster import silhouette_score
from TopicExtractor import TopicExtractor

te = TopicExtractor()
num_topics = 10

topicCollection = []
dic = []

n_topics = []
for i in range(5,num_topics+1):
    n_topics.append(i)

for n in n_topics:
    topicCollection.append(te.getTopicWords(n,100))

for topics in topicCollection:
    for topic in topics:
        for word,_ in topic:
            if word not in topic:
                dic.append(word)

def getTopicsIds(topics):
    ret = []
    for topic in topics:
        t = []
        for word,_ in topic:
            if word in dic:
                t.append(dic.index(word))
        ret.append(t)
    return ret

topicIds =getTopicsIds(topics)
labels = []
for topic in topicIds:
    topicNums = []
    for nr in range(len(topic)):
        topicNums.append(nr)
    labels.append(topicNums)

for i in range(len(topicIds)):
    metric = silhouette_score(topicIds[i],labels[i])
    print(metric)