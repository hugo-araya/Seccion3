# -*- coding: utf-8 -*-

from time import time

def carga_lista():
    lista = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
    return lista

def muestra_lista(lista):
    print ("\nLista ordenada:")
    print (lista, "\n")   

def carga_lista_archivo(n, nombre):
    lista = []
    archivo = open(nombre+".txt")
    for i in range(0,n):
        linea = archivo.readline()
        linea = linea.rstrip("\n")
        lista.append(int(linea))
    return lista
 
def datos(lista):   
    print ("Cantidad de elementos: ", len(lista))
    print ("Tiempo: {0:f} segundos".format(t1 - t0))
    print ("Comparaciones:", comparaciones)   

def shellSort(lista):
    global comparaciones
    n = len(lista)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            val = lista[i]
            j = i
            comparaciones += 1

            while j >= gap and lista[j-gap] > val:
                lista[j] = lista[j-gap]
                j -= gap

            lista[j] = val

        gap = gap// 2

if __name__ == "__main__":
    #lista = carga_lista()
    lista = carga_lista_archivo(500000, "ordenado")
    comparaciones = 0
    t0 = time()
    shellSort(lista)
    t1 = time()
    #muestra_lista(lista)
    datos(lista)
