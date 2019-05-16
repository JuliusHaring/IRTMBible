from sklearn.metrics.cluster import silhouette_score
from sklearn.preprocessing import MinMaxScaler
from TopicExtractor import TopicExtractor

te = TopicExtractor()


num_topics = 20

topicCollection=[]
for i in range(5,num_topics+1):
    topicCollection.append((i,te.getRawNMF(i)))

scores=[]

for i, t in topicCollection:
    nmf, tfidf = t
    model = nmf
    scaler = MinMaxScaler()
    X_sca = scaler.fit_transform(tfidf)
    W = model.fit_transform(X_sca)
    labels = W.argmax(axis=1)
    score = silhouette_score(X_sca, labels)
    scores.append((i,score))

test = scores