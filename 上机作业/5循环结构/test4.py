## 穷举法
## 分析：公鸡最多买：20只，母鸡最多买：33只。设：公鸡x只，母鸡y只，小鸡z只
##  则 0<x<20, 0<y<33, z=100-x-y
count=0
for x in range(0,20):
	for y in range(0,33):
		z=100-x-y
		if 5*x+3*y+z/3 <= 100:
			print('公鸡：%s 母鸡：%s 小鸡：%s'%(x, y, z))
			count+=1
print('总买法:',count)

	
