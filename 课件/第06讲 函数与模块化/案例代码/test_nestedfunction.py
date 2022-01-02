def my_map(iterable, op, value):     #自定义函数
    if op not in '+-*/':
        return 'Error operator'
    def nested(item):                #嵌套定义函数
        return eval(repr(item)+op+repr(value))
    return map(nested, iterable)     #使用在函数内部定义的函数

print(list(my_map(range(5), '+', 5)))#调用外部函数，不需要关心其内部实现
print(list(my_map(range(5), '-', 5)))

f = nested
