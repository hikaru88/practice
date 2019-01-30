class Hexagon:
    def __init__(self, o):
        self.oneside = o

    def calculate_perimeter(self):
        return self.oneside * 6


hexagon1 = Hexagon(5)
print(hexagon1.calculate_perimeter())
