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

def particion(lista, izq, der):
    global comparaciones
    pivote = lista[der]
    indice = izq

    for i in xrange(izq, der):
	comparaciones += 1
		
	if lista[i] <= pivote:
	    lista[indice], lista[i] = lista[i], lista[indice]
	    indice += 1

    lista[indice], lista[der] = lista[der], lista[indice]
    return indice

def quicksort(lista, izq, der):
    if izq < der:
	pivote_indice = particion(lista, izq, der)
	quicksort(lista, izq, pivote_indice-1)
	quicksort(lista, pivote_indice+1, der)

if __name__ == "__main__":
    lista = carga_lista()
    #lista = carga_lista_archivo(100, "aleatorio")
    comparaciones = 0
    t0 = time()
    quicksort(lista, 0, len(lista)-1)
    t1 = time()
    muestra_lista(lista)
    datos(lista)