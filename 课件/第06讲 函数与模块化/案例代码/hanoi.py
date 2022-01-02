def move(n, s, d):
    print("{0}\t{1}-->{2}".format(n, s, d))

def hanoi(n, x, y, z):
    if n==1:
        move(n, x, z)
    else:
        hanoi(n-1, x, z, y)
        move(n, x, z)
        hanoi(n-1, y, x, z)

hanoi(3, 'X', 'Y', 'Z')
