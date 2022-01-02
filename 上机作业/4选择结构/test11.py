import math
x=float(input('请输入x:'))
if(x>=0):y=(x**2-3*x)/(x+1)+2*math.pi+math.sin(x)
else:y=math.log(-5*x)+6*math.sqrt(abs(x)+math.e**4)-(x+1)**3
print(str.format("x={0:.1f},y={1:.14f}",x,y))
