ceruno = "01"
nb = ""
ok = True
while len(nb)!= 8 or ok != False:
    nb = input("Ingrese numero binario: ")
    ok = False
    for carac in nb:
        if carac not in ceruno:
            ok = True

suma = 0
i = 0
while i < len(nb):
    suma = suma + int(nb[i])*2**(7-i)
    i = i +1
print (suma)
