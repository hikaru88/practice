class Shape:
    def what_am_i(self):
        return "I am a shape"



class Rectangle(Shape):
    def __init__(self, len, side):
        self.length = len
        self.side = side

    def calculate_perimeter(self):
        return self.length * 2 + self.side * 2



class Square(Shape):
    def __init__(self, len):
        self.length = len

    def calculate_perimeter(self):
        return self.length * 4

    def change_size(self, long):
        self.long = long
        self.length = self.length + long



rectangle1 = Rectangle(5, 8)
square1 = Square(7)

print(rectangle1.calculate_perimeter())
print(square1.calculate_perimeter())

square1.change_size(3)
print(square1.calculate_perimeter())

square1.change_size(-7)
print(square1.calculate_perimeter())


print(square1.what_am_i())
print(rectangle1.what_am_i())
