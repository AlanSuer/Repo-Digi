list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]

for i in range(1, len(list_num)):
    actual = list_num[i]
    j = i - 1

    while j >= 0 and list_num[j] > actual:
        list_num[j + 1] = list_num[j]
        j -= 1

    list_num[j + 1] = actual

print(list_num)