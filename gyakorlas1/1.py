def haho():
    for x in range(10,221):
        if x%5 == 0 and x%11== 0:
            print("Hahó!")
        elif x%5 == 0:
            print("Ha!")
        elif x%11 == 0:
            print("Hó!")
        else:
            print(x)
haho()