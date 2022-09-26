def desorden(linea):
    acumulaDesorden = 0
    i = 0
    while i < len(linea)-1:
        j = i + 1
        while j < len(linea):
            if linea[i] > linea[j]:
                acumulaDesorden = acumulaDesorden + 1
            j = j + 1
        i = i + 1
    return acumulaDesorden

if __name__ == '__main__':
    lista = ['TTTTGGCCAA','CCCGGGGGGA','TTTGGCCAAA','GATCAGATTT','AACATGAAGT','ATCGATGCAT']
    salida = []
    for l in lista:
        d = desorden(l)
        salida.append([l, d])
    print(salida)


