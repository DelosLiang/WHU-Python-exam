import math

class Ball:
    def __init__(self, radius):
        self.radius = radius

    def surfaceArea(self):
        return 4*math.pi*self.radius**2

    def volume(self):
        return 4/3*math.pi*self.radius**3


def main():
    r = float(input('Enter the radius of a ball: '))
    ball = Ball(r)

    print('Surface area: {0:.2f}'.format(ball.surfaceArea()))
    print('Volume: {0:.2f}'.format(ball.volume()))

if __name__=='__main__':
    main()
