import math

class Cicle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pow(self.radius, 2) * math.pi

    def circumference(self):
        return self.radius * 2 * math.pi



cicle1 = Cicle(7)
print(cicle1.radius)
print(cicle1)

print(cicle1.area())
print(cicle1.circumference())
