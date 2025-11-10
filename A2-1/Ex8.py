list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]

num = int(input("Introdueix un número: "))

trobat = False

for x in list_num:
    if x == num:
        trobat = True

if trobat:
    print("El numero esta dins de la llista")
else:
    print("El numero NO esta dins de la llista")