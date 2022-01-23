from szamolas import Szamolas
from datetime import datetime

class Fajlbair:
    def __init__(self, n, nev):
        self.n = n
        self.nev = nev
    
    def adokivetes(self):
        self.ado = Szamolas(self.n)
        self.ado.ado()
        now = datetime.now()
        date = now.strftime("%Y.%m.%d")
        f = open("györgyi_kristóf.txt", "w")
        f.write(f"Adó kalkulátor\Vásárló neve: {self.nev}\nIngatlan értéke: {self.n}\nFizetendő adó: {self.ado.ingatlan}\n\nKelt: Szeged, {date}")