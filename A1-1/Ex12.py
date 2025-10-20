text = "Hello World"
text2 = "Hola mon!!!"
contador = 0
for i in range(len(text)):
    if text[i] == text2[i]:
        contador = contador + 1
print ("Los textos coinciden en",contador,"letras")
