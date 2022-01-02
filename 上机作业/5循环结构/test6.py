##求2~1000所有完数
for n in range(2,1001):
    result=0
    for i in range(1,n):
        if(n%i==0):#找约数
            result+=i#约数求和
    if(result==n):print(n)

