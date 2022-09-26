def desorden(linea):
    acumulaDesorden = 0
    i = 0
    while i < len(linea)-1:
        carac = linea[i]
        j = i + 1
        while j < len(linea):
            if carac > linea[j]:
                acumulaDesorden = acumulaDesorden + 1
            j = j + 1
        i = i + 1
    return acumulaDesorden

if __name__ == '__main__':
    lista = ['TTTTGGCCAA','CCCGGGGGGA','TTTGGCCAAA','GATCAGATTT','AACATGAAGT','ATCGATGCAT']
    salida = []
    for l in lista:
        d = desorden(l)
        if d < 10:
            dd = '0'+str(d)
        else:
            dd = str(d)

        salida.append(dd+l)
    print(salida)
    salida.sort()
    print(salida)
    for elem in salida:
        print(elem[2:])
        
