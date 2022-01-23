import random

game_on = True
tries = 4
random_num = random.randint(100,110)

def kitalalos_game(input_szam):
    global game_on
    global tries

    if input_szam > random_num:
        print("A random szám kevesebb")
        tries -=1
    elif input_szam < random_num:
        print("A random szám nagyobb")
        tries -=1
    else:
        print("Egy találatos szelvény!")
        game_on = False

while game_on:
    if tries > 0:
        input_num = input("Találd ki a számot(100-110): ")
        if input_num.isnumeric():
            input_to_num = int(input_num)
            if input_to_num >= 100 or input_to_num <= 110:
                kitalalos_game(input_to_num)
            else:
                print("Nincs a tartományban a bekért szám!")
                tries -=1
        else:
            print("Számot adj meg!")
            tries-=1
    else:
        print(f"Vesztettél, béna vagy!")
