j=0

for i in range(2000,3000+1):
    if((i % 4 == 0 and i % 100 != 0) or i % 400 == 0):print(str.format('{0:<5}',i),end="")
    else:continue
    
    j+=1
    if(j%18==0):print()
    
    
