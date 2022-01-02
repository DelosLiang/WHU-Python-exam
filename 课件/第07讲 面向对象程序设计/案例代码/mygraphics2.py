"""
创建自己的图形库（绘图版）
ZhangHua @ 20190706
"""

import abc
import math
import turtle as tt


class Point:
    """点"""
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Shape(metaclass=abc.ABCMeta):
    """形状抽象类，是形状类族的根类"""
    def __init__(self, p):
        self.__pos = p  # 形状的位置，Point对象

    def __getPos(self):
        return self.__pos

    def __setPos(self, p):
        self.__pos = p

    pos = property(__getPos, __setPos)

    @abc.abstractmethod
    def drawme(self, pen):
        pass


class Circle(Shape):
    """圆"""
    def __init__(self, p, r):
        Shape.__init__(self, p)  # p是圆心
        self.radius = r

    def drawme(self, pen):
        pen.circle(self.radius)


class Rect(Shape):
    """矩形"""
    def __init__(self, p, w, h):
        Shape.__init__(self, p)  # p是左上角
        self.width = w
        self.height = h

    def drawme(self, pen):
        for i in range(2):
            pen.forward(self.width)
            pen.right(90)
            pen.forward(self.height)
            pen.right(90)


def drawShape(pen, shape):
    """此函数可以体现类族的多态性"""
    pen.penup()
    startp = shape.pos
    pen.goto(startp.x, startp.y)
    pen.pendown()
    shape.drawme(pen)


def painter():
    pen = tt.Turtle()
    pen.pencolor("red")
    pen.pensize(3)

    c1 = Circle(Point(0, 0), 50)
    drawShape(pen, c1)

    pen.pencolor("blue")
    r1 = Rect(Point(-90, -50), 180, 60)
    drawShape(pen, r1)

    tt.done()


if __name__=="__main__":
    painter()
