textdna = "atggatcattta"
letra = "a"
contador = 0
for i in range(len(textdna)):
    if textdna[i] == letra:
        contador = contador + 1
        print("Letra encontrada en la posicion: ",i)
print("Total de veces que parece la letra", letra, "es:", contador)