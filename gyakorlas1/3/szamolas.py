class Szamolas:
    kerulet = 0
    terulet = 0

    def __init__(self, h1, h2, h3):
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3
        self.kerulet = 0
        self.terulet = 0

    def szamitos(self):
        self.kerulet = self.h1 + self.h2 + self.h3
        self.terulet = (self.h1*self.h2)/2
        



