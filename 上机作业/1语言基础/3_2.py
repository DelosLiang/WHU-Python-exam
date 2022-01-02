def getValue(b,r,n):
    v=b*((1+r)**n)
    return v
b=float(input("请输入本金b:"))
r=float(input("请输入年利率r:"))
n=float(input("请输入年数n:"))
total=getValue(b,r,n)
print("最终受益:","%.2f" %total )
