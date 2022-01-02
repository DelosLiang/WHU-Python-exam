def fun(a,b):
    print(a,b)
    
fun(5,2)

#c=8命名参数，*p接收多个变长参数，**q接收多个命名的变长参数
def func(a,b,c=8,**q):
    print(q)
func(b=5,c=2,a=9,d=9,e=1,gjh=2)

def fun1(a,b):
    return func2(a+b)
def func2(a):
    return a*a
c = fun1(3,1)
print(c)

'''
def fun(a)
    b=a+2
fun(3)
print(b)
会报错b没有定义的原因是：下面的print(b)是在函数外定义，访问不了函数内的内容（作用域的问题）
'''

'''
在一个源代码文件中，在函数和类定义之外声明的变量。
全局变量的作用域为其定义所在的模块，从定义的位置起，直到文件结束位置。
如果在函数中定义的局部变量与全局变量同名，则局部变量屏蔽全局变量。
（就近原则）
eg:
'''
x = 9
def fun():
    x=3
    print(x)
fun()