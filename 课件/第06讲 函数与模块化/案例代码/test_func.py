def f1():
    a=input()
    if a in ['a', 'A']:
        x=True
    else:
        x=False

    def innerf():
        if 2>3:
            nonlocal x
            x+=10
        else:
            #nonlocal x
            x+=5
        print(x)

    global y
    y=100
    
    innerf()
    return x

def test_f1():
    f1()
    # innerf()
    print(y)


def IsPerfectNumber(n):
    a=list(range(1,n+1))
    for i in a:
        b=list(range(1,i+1))
        c=[j for j in b if i%j==0]
        if sum(c)==i:
            return i

def test_IsPerfectNumber():
    n=int(input())
    print(IsPerfectNumber(n), end=' ')

test_IsPerfectNumber()
