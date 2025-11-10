list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
print(list_num)
i = len(list_num) - 1

while i>=0:
    if list_num.count(list_num[i]) > 1:
        list_num.pop(i)
    i -= 1
    
print(list_num)