class Animal(object):  # 定义基类
    def show(self):
        print('I am an animal.')


class Cat(Animal):  # 派生类，继承了基类的show()方法
    def show(self):
        super(Cat, self).show()   # 或者 Animal.show()
        print('In fact, I am a cat.')


Cat().show()
