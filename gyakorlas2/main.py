from szamolas import *

input_szam = input("Szám: ")
szam = int(input_szam)

szamolas = Osztaly(szam)
szamolas.szamolas()

print(szamolas.number)
print(szamolas.terulet)
print(szamolas.kerulet)
