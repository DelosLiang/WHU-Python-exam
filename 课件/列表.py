ls=[1,2,3,5]
for i in ls:
    print(i,end=' ')
#分离列表#

print('\n')

for i in range(len(ls)):
    print(i,end=':')
    print(ls[i],end=' ')
#i对应索引位置，end对应具体的值#

print('\n')

for i,x in enumerate(ls):
    print(i,x,sep=' ',end=', ')
'''
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
>>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

>>> list(enumerate(seasons, start=1))       # 下标从 1 开始
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
'''