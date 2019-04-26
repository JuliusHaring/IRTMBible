from TopicExtractor import TopicExtractor

te = TopicExtractor()

testaments = ["",""]
books = te.books

for i in range(len(books)):
    book = books[i]
    for chapter in book:
        for sentence in chapter:
            if i < 39:
                testaments[0] = testaments[0] + sentence + "\n "
            else:
                testaments[1] = testaments[1] + sentence + "\n "

print(testaments)