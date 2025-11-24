frase = input("Escribe una frase: ")

frase = frase.lower()

paraules = frase.split()

freq = {}

for paraula in paraules:
    if paraula in freq:
        freq[paraula] += 1
    else:
        freq[paraula] = 1

print(freq)