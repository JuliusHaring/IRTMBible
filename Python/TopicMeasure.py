from sklearn.metrics.cluster import silhouette_score
from TopicExtractor import TopicExtractor


te = TopicExtractor()

topicCollection=[]
for i in [10,20,30,40,50,60,70,80,90,100,200]:
    topicCollection.append((i,te.getRawNMF(i)))

scores=[]

for i, t in topicCollection:
    nmf, tfidf = t
    model = nmf
    W = model.fit_transform(tfidf)
    labels = W.argmax(axis=1)
    score = silhouette_score(tfidf, labels)
    scores.append((i,score))
    

print(scores)