preus = {
    'motxila': 45,
    'llapis': 1,
    'calculadora': 25
}

preus_final = {}

for producte, preu in preus.items():
    if preu > 20:
        preus_final[producte] = preu

print(preus_final)