import math
x=float(input("请输入一个角度值:"))
y=float(input("请输入另一个角度值:"))
s=2*math.sin((x+y)/2/180*math.pi)*math.cos((x-y)/2/180*math.pi)
print(str.format('2sin(({:.1f}+{:.1f})/2)cos(({:.1f}-{:.1f})/2)={:.3f}',x,y,x,y,s))
