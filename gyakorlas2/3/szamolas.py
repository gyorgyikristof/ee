class Szamolas():
    kerulet = 0
    terulet = 0

    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2
        self.kerulet = 0
        self.terulet = 0

    def szamitos(self):
        self.kerulet = 2*(self.t1+self.t2)
        self.terulet = self.t1*self.t2

