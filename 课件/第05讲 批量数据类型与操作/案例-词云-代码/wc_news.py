'''
创建新闻报道的词云
'''
import jieba
import wordcloud

f = open('坚持以生为本 助推学生发展.txt', 'r', encoding='utf-8')
txt = f.read()
f.close()

wordList = jieba.lcut(txt)
wcstr = ' '.join(wordList)

wc = wordcloud.WordCloud(
    'msyh.ttc', width=640, height=480,
    background_color='white',
    max_words=50)

wcim = wc.generate(wcstr)
wcim.to_image().save('wc_news.png')
                         
    
