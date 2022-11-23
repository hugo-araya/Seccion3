# -*- coding: utf-8 -*-

from time import time

def carga_lista():
    lista = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
    return lista

def muestra_lista(lista):
    print "\nLista ordenada:"
    print lista, "\n"  

def carga_lista_archivo(n, nombre):
    lista = []
    archivo = open(nombre+".txt")
    for i in range(0,n):
        linea = archivo.readline()
        linea = linea.rstrip("\n")
        lista.append(int(linea))
    return lista

def datos(lista):   
    print "Cantidad de elementos: ", len(lista)
    print "Tiempo: {0:f} segundos".format(t1 - t0)
    print "Comparaciones:", comparaciones  

def selectionSort(lista):
    global comparaciones
    n = len(lista)

    for i in xrange(n - 1):
        menor = i
        comparaciones += 1

        for j in xrange(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j

        lista[i], lista[menor] = lista[menor], lista[i]

if __name__ == "__main__":
    lista = carga_lista()
    #lista = carga_lista_archivo(100, "aleatorio")
    comparaciones = 0
    t0 = time()
    selectionSort(lista)
    t1 = time()
    muestra_lista(lista)
    datos(lista)