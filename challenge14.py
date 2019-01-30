class Square:
    square_list = []

    def __init__(self, len):
        self.length = len
        Square.square_list.append((self))

    def print(self):
        print("{} by {} by {} by {}".format(self.length, self.length, self.length, self.length))


square1 = Square(30)
square2 = Square(58)

print(Square.square_list)

square1.print()
