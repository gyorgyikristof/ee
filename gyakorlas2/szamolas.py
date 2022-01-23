class Osztaly:
    
    def __init__(self,szam):
        self.number = szam
        self.kerulet = 0
        self.terulet = 0

    def szamolas(self):
        self.kerulet = 4*self.number
        self.terulet =self.number*self.number
        print(f"Lokális: {self.kerulet}, {self.terulet}")



