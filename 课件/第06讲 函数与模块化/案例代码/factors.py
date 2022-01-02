from random import randint

def factors(num, fac=[]):
    #每次都从2开始查找因数
    for i in range(2, int(num**0.5)+1):
        #找到一个因数
        if num%i == 0:
            fac.append(i)
            #对商继续分解，重复这个过程
            factors(num//i, fac)
            #注意，这个break非常重要
            break
    else:
        #不可分解了，自身也是个因数
        fac.append(num)

facs = []
n = randint(2, 10**8)
factors(n, facs)
result = '*'.join(map(str, facs))
if n==eval(result):
    print(n, '= '+result)
