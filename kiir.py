from szamolas import Szamolas
from datetime import datetime


class Kiir:
    def __init__(self, h1, h2, h3, nev):
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3
        self.nev = nev

    def kiiras(self):
        self.szamitos = Szamolas(self.h1, self.h2, self.h3)
        self.szamitos.szamitos()
        now = datetime.now()
        date = now.strftime("%Y.%m.%d")
        f = open("györgyi_kristof.txt", "w")
        f.write(f"Számításos lap\nFelhasználó neve: {self.nev}\na oldal {self.h1} m\nb oldal {self.h2} m\nc oldal {self.h3} m\nKerulet: {self.szamitos.kerulet} m\nTerulet: {self.szamitos.terulet} m2\n\nKelt: Szeged,{date}")

