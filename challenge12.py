class Apple:
    def __init__ (self, w, c):
        self.weight = w
        self.color = c
        self.rot = 0
        print("Created!")

    def status (self, t, d):
        self.temperature = t
        self.days = d
        self.rot = t * d


apple1 = Apple(200, "red")
print(apple1.color)
apple1.status(29, 5)
print(apple1.rot)
