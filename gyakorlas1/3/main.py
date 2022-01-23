from kiir import Kiir

nev = input("Add meg a neved!: ")
h1 = input("Add meg a háromszög első oldalának hosszát!: ")
h2 = input("Add meg a háromszög második oldalának hosszát!: ")
h3 = input("Add meg a háromszög harmadik oldalának hosszát!: ")

if h1.isnumeric() or h2.isnumeric() or h3.isnumeric():
    h1i = int(h1)
    h2i = int(h2)
    h3i = int(h3)
    nyomtatas = Kiir(h1i, h2i, h3i, nev)
    nyomtatas.kiiras()

else:
    print("Nem számot adtál meg!")

        