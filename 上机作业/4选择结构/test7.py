sum_1=0;sum_2=0
n=int(input('请输入n的值:'))
for i in range(1,n+1):
    if((i-1)%4==0):sum_1+=i
    elif(i%2==0):continue
    else:sum_2-=i
print('Sn=',sum_1+sum_2)
    
