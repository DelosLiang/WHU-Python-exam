class Animal(object):  # 定义基类
    def show(self):
        print('I am an animal.')


class Pet():
    def __init__(self, name):
        self.nickname = name


class Cat(Animal, Pet):  # 多重继承
    def __init__(self, name):
        # 调用基类的构造函数对基类数据成员进行初始化
        super(Cat, self).__init__(name)
        # 或者 Pet.__init__(self, name)

    def show(self):
        super(Cat, self).show()   # 或者 Animal.show()
        print('In fact, I am a cat.')
        print('My nickname is '+self.nickname+'.')


Cat('Tom').show()
