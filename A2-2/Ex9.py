alumnes = {
    'Marta': {'edat': 18, 'nota_final': 8.5},
    'Joan': {'edat': 19, 'nota_final': 6.7}
}

alumne_millor = {}
millor_nota = -1

for nom, dades in alumnes.items():
    if dades['nota_final'] > millor_nota:
        millor_nota = dades['nota_final']
        alumne_millor = nom

print(alumne_millor)