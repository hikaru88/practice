class Horse:
    def __init__(self, name, color, price, owner):
        self.name = name
        self.color = color
        self.price = price
        self.owner = owner



class Rider:
    def __init__(self, name):
        self.name = name



Hikaru = Rider("Hikaru Sato")
Pichan = Horse("Pi-chan", "blue", "2000", Hikaru)

print(Pichan.owner.name)
