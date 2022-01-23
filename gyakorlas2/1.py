def kame_hame():
    for x in range(1,411):
        if x%4==0 and x%10==0:
            print("Kame Hame!")
        elif x%4==0:
            print("Kame!")
        elif x%10==0:
            print("Hame!")
        else:
            print(x)

kame_hame()