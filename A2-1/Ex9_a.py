list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]

ordenada = []

while len(list_num) > 0:
    minim = list_num[0]

    for x in list_num:
        if x < minim:
            minim = x

    ordenada.append(minim)

    list_num.remove(minim)

print(ordenada)