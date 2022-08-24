nombre = input("Nombre: ")
ascii = []
for letra in nombre:
    ascii.append(ord(letra))
    print(ord(letra))

for numero in ascii:
    print(chr(numero))

