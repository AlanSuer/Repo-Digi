paraula = input("Introdueix una paraula: ")

freq = {}

for lletra in paraula:
    if lletra in freq:
        freq[lletra] += 1
    else:
        freq[lletra] = 1

print(freq)