n1=int(input("请输入第一个公约数："))
n2=int(input("请输入第二个公约数："))
r=n1%n2
print(str.format('{0}和{1}的最大公约数为',n1,n2),end="")

while(r!=0):
    n1=n2
    n2=r
    r=n1%n2

print(n2)
        
