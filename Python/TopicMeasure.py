from sklearn.metrics.cluster import silhouette_score
from TopicExtractor import TopicExtractor


te = TopicExtractor()

topicCollectionNMF=[]
topicCollectionLDA=[]
for i in [10,20]:
    topicCollectionLDA.append((i,te.getRawLDA(i)))
    topicCollectionNMF.append((i,te.getRawNMF(i)))

scoresNMF=[]
scoresLDA=[]

for i, t in topicCollectionNMF:
    nmf, rep = t
    model = nmf
    W = model.fit_transform(rep)
    labels = W.argmax(axis=1)
    score = silhouette_score(rep, labels)
    scoresNMF.append((i,score))
    
for i, t in topicCollectionLDA:
    nmf, rep = t
    model = nmf
    W = model.fit_transform(rep)
    labels = W.argmax(axis=1)
    score = silhouette_score(rep, labels)
    scoresLDA.append((i,score))


print(scoresNMF)
print(scoresLDA)