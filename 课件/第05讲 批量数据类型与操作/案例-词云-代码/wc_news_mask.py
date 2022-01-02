'''
创建新闻报道的词云
'''
import jieba
import wordcloud
from imageio import imread

f = open('坚持以生为本 助推学生发展.txt', 'r', encoding='utf-8')
txt = f.read()
f.close()

wordList = jieba.lcut(txt)
wcstr = ' '.join(wordList)

maskim = imread('whulib-logo.jpg')

wc = wordcloud.WordCloud(
    'msyh.ttc', width=640, height=480,
    background_color='white', mask=maskim)

wcim = wc.generate(wcstr)
wcim.to_image().show() #save('wc_news_whulib.png')
                         
    
