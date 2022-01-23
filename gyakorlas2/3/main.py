from kiir import Kiir

nev = input("Add meg a neved!: ")
t1 = input("Add meg a téglalap a oldalának hosszát!: ")
t2 = input("Add meg a téglalap b oldalának hosszát!: ")

if t1.isnumeric() or t2.isnumeric():
    t1i = int(t1)
    t2i = int(t2)
    nyomtatas = Kiir(t1i, t2i, nev)
    nyomtatas.nyomtatas_funkcio()
