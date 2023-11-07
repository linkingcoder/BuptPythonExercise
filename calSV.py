import math


class Rect:
    def __init__(self, l, h, z):
        self.l = l
        self.h = h
        self.z = z

    def length(self):
        return 2 * (self.l + self.h)

    def area(self):
        return self.l * self.z * self.h


class Cubic(Rect):
    def V(self):
        return self.h * self.l * self.z

    def area(self):
        return 2 * (self.h * self.l + self.h * self.z + self.z * self.l)


class Pyramid(Rect):
    def V(self):
        return self.l * self.z * self.h / 3.0

    def area(self):
        return self.l * self.h + self.l * math.sqrt(self.z * self.z + self.h * self.h/4) + self.h * math.sqrt(
            self.z * self.z + self.l * self.l/4)


while True:
    try:
        a, b, c = input().split()
        flag = True
        a = float(a)
        b = float(b)
        c = float(c)
        if a <= 0 or b <= 0 or c <= 0:
            flag = False
            print('0.00 0.00 0.00 0.00')
        if flag:
            m = Cubic(a, b, c)
            n = Pyramid(a, b, c)
            print('%.2f %.2f %.2f %.2f' % (m.area(), m.V(), n.area(), n.V()))
    except:
        break