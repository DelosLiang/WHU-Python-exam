# 统计《三国演义》中出场次数最多的10个人物
import jieba
f = open('threekingdoms.txt', 'r', encoding='utf-8')
txt = f.read()

wordList = jieba.cut(txt)
wordDict = dict()
for word in wordList:
    if len(word)!=1:
        wordDict[word] = wordDict.get(word, 0)+1

items = list(wordDict.items())
items.sort(key=lambda x:x[1], reverse=True)

for i in range(10):
    word, count = items[i]
    print("{0:<10}({1:>5})".format(word, count))
