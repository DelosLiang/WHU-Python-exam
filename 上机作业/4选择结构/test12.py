import math
a=float(input('请输入系数a:'))
b=float(input('请输入系数b:'))
c=float(input('请输入系数c:'))
if(a==0 and b==0):print('此方程无解!')
elif(a==0 and b!=0):print(str.format('此方程的解为：{0:.1f}',-c/b))
elif(b**2-4*a*c==0):print(str.format('此方程有两个相等实根：{0:.1f}',-b/(2*a)))
elif(b**2-4*a*c>0):print(str.format('此方程有两个不等实根：{0:.1f}和{1:.1f}',-b/(2*a)+math.sqrt(b**2-4*a*c)/(2*a),-b/(2*a)-math.sqrt(b**2-4*a*c)/(2*a)))
else:print(str.format('此方程有两个不等实根：{0:.1f}+{1:.1f}i和{2:.1f}-{3:.1f}i',-b/(2*a),math.sqrt(-b**2+4*a*c)/(2*a),-b/(2*a),math.sqrt(-b**2+4*a*c)/(2*a)))
