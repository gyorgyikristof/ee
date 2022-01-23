from fajlbair import Fajlbair

nev = input("Add meg a neved!: ")
szam = input("Add meg az ingatlanod értékét!: ")
if szam.isnumeric():
    n = int(szam)
    nyomtatas = Fajlbair(n, nev)
    nyomtatas.adokivetes()
else: print("Nem számot adtál meg!")
