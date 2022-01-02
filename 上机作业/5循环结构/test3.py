##求最大公约数和最小公倍数
import random
m=random.randint(0,100);n=random.randint(0,100)#生成两个0~100随机整数
m1=m;n1=n#方便最后最小公倍数的计算
print(str.format('整数1={0},整数2={1}',m1,n1))
if(m>n):pass
else:
    t=m
    m=n
    n=t
#对于一致的两个正整数，使得m>=n
r=m%n#m除以n得余数r
while(r!=0):
    m=n
    n=r
    r=m%n
#若r!=0,则将n的值赋给m，将r的值赋给n，继续相除得到新的余数r。最后的n就是最大公约数
print(str.format('最大公约数={0}，最小公倍数={1}',n,int(m1*n1/n)))#最小公倍数就是已知的两个正整数之积除以最大公约数的商
