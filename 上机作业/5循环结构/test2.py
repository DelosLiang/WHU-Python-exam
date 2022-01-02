##while/for循环求阶乘二合一
x=1
while True:
    n=int(input("请输入非负整数："))
    if(n>0):
        for i in range(1,n):
            x*=i+1
        print(str.format("while/for循环：{0}！={1}",n,x))#对输入的非负值进行阶乘运算
        break
    elif(n==0):
        print("while/for循环:0!=1")#特别地，0！=1
        break
    else:
        continue#如果输入的是负整数，则继续提示输入非负整数

    
        
