from TopicExtractor import TopicExtractor
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import urllib
import requests

te = TopicExtractor()

books = []

temp = te.books
for book in temp:
    content = ""
    for chapter in book:
        for sentence in chapter:
            content += sentence +"\n"
    books.append(content)
    
book_names = te.book_names
STOPWORDS.add('wa')
def generate_wordcloud(words, mask, book_name): 
    word_cloud = WordCloud(width = 512, height = 512, background_color='white', stopwords=STOPWORDS, mask=mask, random_state=1).generate(words)
    fig = plt.figure(figsize=(10,8),facecolor = 'white', edgecolor='blue')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig('./Resources/WordClouds/'+book_name+".png", dpi=fig.dpi)
    plt.close()

mask = np.array(Image.open('./Resources/WordClouds/masks/cross_little.png'))
c = 0
for book in books:
    generate_wordcloud(book, mask, book_names[c])
    c+=1