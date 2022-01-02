for i in range(1,10):
    for j in range(1,10):
        if i <= j:
            if j != 9:
                if j <= 3:
                    print('{0}*{1}={2:<1} '.format(i,j,i*j),end='')
                else:
                    print('{0}*{1}={2:<2} '.format(i,j,i*j),end='')
            else:
                print('{0}*{1}={2:<2} '.format(i,j,i*j))
        else:
            if j <= 3:
                print('{0} {1} {2:<1} '.format(' ',' ',' '),end='')
            else:
                print('{0} {1} {2:<2} '.format(' ',' ',' '),end='')

for i in range(1,10):
    line=''
    for j in range(1,i+1):
        if i*j>9 or j==1:
            line+='{0}*{1}={2} '.format(j,i,i*j)
        else:
            line+='{0}*{1}={2}  '.format(j,i,i*j)
    print(line)
