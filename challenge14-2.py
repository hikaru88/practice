class People:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def comparison(self):
        if self.name is "Hikaru":
            print(True)
        else:
            print(False)
        if self.nationality is "Japanese":
            print(True)
        else:
            print(False)


Hikaru = People("Hikaru", "Japanese")
Hikaru.comparison()

Mikeru = People("Mikeru", "America")
Mikeru.comparison()

Takeshi = People("Takeshi", "Japanese")
Takeshi.comparison()
