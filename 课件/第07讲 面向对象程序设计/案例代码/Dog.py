class Dog:
    __name = "狗" # 类属性
    __count = 0   # 类属性

    def __new__(cls, *args, **kwargs): # 该方法在__init__()之前被调用
        if cls.__count>=3:
            raise Exception("最多只能有3条"+cls.__name)
        else:
            return object.__new__(cls)
    
    def __init__(self, name): # 构造方法
        self.name = name
        Dog.__count += 1
        
    def bark(self): # 一般实例方法
        print("汪!汪!汪!", self.name+"在这里。")

    @classmethod            # 定义类方法的装饰器
    def animal_name(cls):   # 类方法
        return cls.__name

    @staticmethod           # 定义静态方法的装饰器
    def dog_count():        # 静态方法
        return Dog.__count

    @classmethod
    def set_animal_name(cls, name):
        cls.__name = name

def main():
    dog1 = Dog("阿黄")
    dog1.bark()
    print(dog1.name+"是一条"+dog1.animal_name())
    print("现在有", dog1.dog_count(), "条"+dog1.animal_name())

    Dog.set_animal_name("中华田园犬")

    dog2 = Dog("阿黑")
    Dog.bark(dog2) # 通过类名来调用实例方法，需要把对象名作为self参数的实参
    print(dog2.name+"是一条"+dog2.animal_name())

    dog3 = Dog("白雪")
    print(dog3.name+"是一条"+dog3.animal_name())
    print("现在有", Dog.dog_count(), "条"+Dog.animal_name())

    dog4 = Dog("不可能")

if __name__=='__main__':
    main()
