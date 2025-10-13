nombre1 = 15 
nombre2 = 9
nombre3 = 12

if nombre1 >= nombre2 and nombre1 >= nombre3:
    major = nombre1
elif nombre2 >= nombre1 and nombre2 >= nombre3:
    major = nombre2
else:
    major = nombre3

print("El numero mes gran es", major)