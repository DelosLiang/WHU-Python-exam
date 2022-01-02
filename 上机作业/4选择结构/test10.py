import math
a,b,c=map(float, input("请输入三角形的三边长：").split())
if(a+b>c and a+c>b and b+c>a and a,b,c>0):
    L=a+b+c
    h=L/2
    S=math.sqrt(h*(h-a)*(h-b)*(h-c))
    print(str.format("周长为：{0}，面积为：{1}",L,S))
else:print("输入的三条边无法构成三角形")
