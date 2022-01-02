# 统计《哈姆雷特》文本文件中出现的次数最多的10个单词
f = open('hamlet.txt', 'r')
txt = f.read()
txt = txt.lower()
for c in '\'\"\\-!?$%()<>=_|{}~,;./*&@^':
    txt = txt.replace(c, ' ')
    
wordList = txt.split()
wordDict = dict()
for word in wordList:
    wordDict[word] = wordDict.get(word, 0)+1

items = list(wordDict.items())
items.sort(key=lambda x:x[1], reverse=True)

for i in range(10):
    word, count = items[i]
    print("{0:<20}({1:>5})".format(word, count))
