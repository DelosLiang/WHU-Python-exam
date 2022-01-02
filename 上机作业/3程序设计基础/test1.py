n1=int(input("请输入第一个公约数："))
n2=int(input("请输入第二个公约数："))
r=n2

while(n1 % r != 0 or n2 % r != 0):
    r = r - 1
print(str.format('{0}和{1}的最大公约数为{2}',n1,n2,r))

