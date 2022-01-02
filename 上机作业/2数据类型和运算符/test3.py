import math
r1=eval(input("请输入外圆半径："))
r2=eval(input("请输入内圆半径："))
S=math.pi*(r1**2-r2**2)
print("圆环的面积为：","%.2f"%(S))
   
