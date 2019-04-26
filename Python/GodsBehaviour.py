from TopicExtractor import TopicExtractor
from nltk import word_tokenize
from nltk import pos_tag as pos_tag

te = TopicExtractor()

testaments = ["",""]
books = te.getFullTextBooks()

for i in range(len(books)):
    book = books[i]
    for chapter in book:
        for sentence in chapter:
            if i < 39:
                testaments[0] = testaments[0] + sentence + "\n "
            else:
                testaments[1] = testaments[1] + sentence + "\n "

tagged = []
tagged.append(pos_tag(word_tokenize(testaments[0])))
tagged.append(pos_tag(word_tokenize(testaments[1])))

print(tagged)