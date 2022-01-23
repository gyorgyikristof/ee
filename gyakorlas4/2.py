import random

jatekban_van = True
t = 3
r = random.randint(201,210)

def talalgatos_game(i):
    global jatekban_van
    global t

    if i > r:
        print("A random szám kevesebb")
        t-=1
    elif i < r:
        print("A random szám több")
        t-=1
    else:
        print("Nyerő!")
        jatekban_van = False

while jatekban_van:
    if t > 0:
        i = input("Találd ki a számot(201-210):")
        if i.isnumeric():
            inti = int(i)
            if inti >=201 and inti <=210:
                talalgatos_game(inti)
            else:
                print("Nincs tartományban a bekért szám")
                t-=1
        else:
            print("Számot adj meg!")
            t-=2
    else:
        print(f"Vesztes!")
        jatekban_van = False
    


