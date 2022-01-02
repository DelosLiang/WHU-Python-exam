"""
创建自己的图形库
ZhangHua @ 20190706
"""

import abc
import math


class Shape(metaclass=abc.ABCMeta):
    """形状抽象类，是形状类族的根类"""
    @abc.abstractmethod
    def area(self):
        pass


class Circle(Shape):
    """圆"""
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return "Circle("+str(self.radius)+")"


class Rect(Shape):
    """矩形"""
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    def __str__(self):
        return "Rect("+str(self.width)+","+str(self.height)+")"


def showShapeArea(shape):
    """此函数可以体现类族的多态性"""
    print("{} area is {:.3f}".format(str(shape), shape.area()))


def test_Shape():
    # s = Shape()  # 此句错误，因为抽象类不能实例化，即不能定义抽象类的对象

    c1 = Circle(20)
    showShapeArea(c1)

    r1 = Rect(12, 5)
    showShapeArea(r1)


if __name__ == '__main__':
    test_Shape()
