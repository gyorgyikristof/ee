def ketto_tizenegy():
    for x in range(1,116):
        if x%2==0 and x%11==0:
            print("Kettő Tizenegy!")
        elif x%2==0:
            print("Kettő!")
        elif x%11==0:
            print("Tizenegy!")
        else:
            print(x)

ketto_tizenegy()

