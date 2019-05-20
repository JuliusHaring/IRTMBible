from gensim.models import CoherenceModel
from TopicExtractor import TopicExtractor

def getCohModel(model, corpus, dic):
    cm = CoherenceModel(model=model, corpus=corpus, coherence='u_mass', dictionary= dic)
    return cm.get_coherence()

te = TopicExtractor()

topicCollectionNMF=[]
topicCollectionLDA=[]
for i in [10,20,30,40,50,60,70,80,90,100]:
    topicCollectionLDA.append((i, te.getRawLDA(i)))
    topicCollectionNMF.append((i, te.getRawNMF(i)))

scoresNMF=[]
scoresLDA=[]

for i in range(len(topicCollectionLDA)):
    topicLDA = topicCollectionLDA[i][1]
    scoresLDA.append(getCohModel(topicLDA[0],topicLDA[1], topicLDA[2]))
    topicNMF = topicCollectionNMF[i][1]
    scoresNMF.append(getCohModel(topicNMF[0],topicNMF[1], topicNMF[2]))

x = 0