from TopicExtractor import TopicExtractor
from nltk import word_tokenize
from nltk import pos_tag as pos_tag
from nltk.chunk import RegexpParser
from nltk.stem import WordNetLemmatizer
from collections import Counter, OrderedDict
import matplotlib.pyplot as plt

te = TopicExtractor()

books = te.getFullTextBooks()
tagged = [[],[]]

for i in range(len(books)):
    book = books[i]
    for chapter in book:
        for sentence in chapter:
            if i < 39:
                tagged[0].append(pos_tag(word_tokenize(sentence)))
            else:
                tagged[1].append(pos_tag(word_tokenize(sentence)))


grammar = "Chunk: {<NNP><VB.?>}"
parser = RegexpParser(grammar)

verbs = [[],[]]

for t in range(len(tagged)):
    for sentence in tagged[t]:
        temp = parser.parse(sentence)
        for subtree in temp.subtrees(filter=lambda t: t.label() == 'Chunk'):
                if(str(subtree[0][0]).lower() == "god"):
                    verb = str(subtree[1][0]).lower()
                    verb = WordNetLemmatizer().lemmatize(verb,'v')
                    verbs[t].append(verb)


old_testament_counts = Counter(verbs[0]).most_common()
new_testament_counts = Counter(verbs[1]).most_common()

def plot(D):
    plt.bar(range(len(D)), list(D.values()), align='center')
    plt.xticks(range(len(D)), list(D.keys()))
    plt.show()

plot(old_testament_counts)
plot(new_testament_counts)