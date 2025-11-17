capital_pais = {
    "Espanya": "Madrid",
    "França": "París",
    "Itàlia": "Roma"
}

for pais, capital in capital_pais.items():
    print(f"La capital de {pais} és {capital}.")

pais = input("Introdueix un país: ")

if pais in capital_pais:
    print(f"La capital de {pais} és {capital_pais[pais]}.")
else:
    print(f"El país '{pais}' no es troba al diccionari.")