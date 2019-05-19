from TopicExtractor import TopicExtractor

te = TopicExtractor()

indices = [10,20,30,40,50,60,70,80,90,100]
n_top_words = 10
how_many = 1

topicsNMF = []
topicsLDA = []

for i in indices[:how_many]:
    topicsNMF.append(te.getTopicWords(i,n_top_words))
    topicsLDA.append(te.getTopicWordsLDA(i,n_top_words))

def delta(Ti,Tj):
    c = Ti
    for j in Tj:
        if j not in c:
            c.append(j)
        
    return len(c)

def T(M):
    ret = []
    for topic in M:
        ret.append(topic[0])
    return ret

def DSD(Mi, Mj,k,t=n_top_words):
    Ti = T(Mi)
    Tj = T(Mj)

    return delta(Ti,Tj)/(t*k)

def ADSD(k_topics):
    ADSDs = []
    for n in range(len(indices[:how_many])):
        r=len(indices[:how_many])
        topics = k_topics[n]
        k = indices[n]
        temp = []
        for i in topics:
            for j in topics:
                if i != j:
                    temp.append(DSD(i,j,k))

        calc = 0

        for dsd in temp:
            calc += dsd

        test = 1/(r-(r-1))
        
        calc = calc/(r-(r-1))

        ADSDs.append((k,calc))
    return ADSDs

print(ADSD(topicsLDA))