list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]

for i in range(len(list_num)):
    min_index = i

    for j in range(i + 1, len(list_num)):
        if list_num[j] < list_num[min_index]:
            min_index = j

    temp = list_num[i]
    list_num[i] = list_num[min_index]
    list_num[min_index] = temp

print(list_num)