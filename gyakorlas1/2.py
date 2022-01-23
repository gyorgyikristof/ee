import random

lotto_on = True
tries = 5
random_num = random.randint(1,90)

def kitalalos_game(input_szam):
    global lotto_on
    global tries

    if input_szam > random_num:
        print("A random szám kevesebb")
        tries -=1
    elif input_szam < random_num:
        print("A random szám nagyobb")
        tries -=1
    else:
        print("Egy találatos szelvény!")
        lotto_on = False

while lotto_on:
    if tries > 0:
        input_num = input("Találd ki a számot(1-90):")
        if input_num.isnumeric():
            input_to_num = int(input_num)
            if input_to_num >= 1 and input_to_num <= 90:
                kitalalos_game(input_to_num)
            else:
                print("Nincs tartományban a bekért szám!")
                tries -=1
        else:
            print("Számot adj meg!")
            tries -= 1
    else:
        print(f"0 találatos szelvény!")
        lotto_on = False


