from szamolas import Szamolas
from datetime import datetime

class Kiir():

    def __init__(self, t1, t2, nev):
        self.t1 = t1
        self.t2 = t2
        self.nev = nev

    def nyomtatas_funkcio(self):
        self.szamitos = Szamolas(self.t1, self.t2)
        self.szamitos.szamitos()
        now = datetime.now()
        date = now.strftime("%Y.%m.%d")
        f = open("györgyi_kristof.txt", "w")
        f.write(f"Számításos lap\nFelhasználó neve: {self.nev}\nEgyik oldal hossza: {self.t1} m\nMásik oldal hossza: {self.t2} m\nKerulet: {self.szamitos.kerulet} m\nTerulet: {self.szamitos.terulet} m2\n\nKelt: Szeged,{date}")
        f.close()