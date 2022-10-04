import numpy as np
import os

def limpia_pantalla():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
    
def _muestra(m,n,k,l):
    print('Cantidad de filas   : ', m)
    print('Cantidad de columnas: ', n)
    print('Cantidad de insectos: ', k)
    print('Cantidad de ciclos  : ', l)    

def devuelve_variables(linea):
    lista = linea.split(' ')
    m = int(lista[0])
    n = int(lista[1])
    k = int(lista[2])
    l = int(lista[3])
    return m,n,k,l

def devuelve_tablero(ent, m, n):
    dimensiones=(m,n)
    tablero = np.zeros(dimensiones,dtype = int)
    for linea in ent:
        linea = linea.rstrip('\n')
        lista = linea.split(' ')
        tablero[int(lista[0])][int(lista[1])]=1  
    return tablero

def leer_datos(nombre):
    ent = open(nombre)
    linea = ent.readline().rstrip('\n')
    m, n, k, l = devuelve_variables(linea)
    tablero = devuelve_tablero(ent, m, n)
    mostrar_tablero(tablero, 'De paso')
    ent.close()
    return tablero, l

def mostrar_tablero(tablero, mensaje):
    fc = tablero.shape
    m = int(fc[0])
    n = int(fc[1])
    print()
    print(mensaje)
    for i in range(m):
        for j in range(n):
            print(tablero[i][j], ' ', end ='')
        print()

def vecinos(f, c):
    

def ciclo_evolutivo(tablero, ciclos):
    fc = tablero.shape
    m = int(fc[0])
    n = int(fc[1])
    dimensiones=(m,n)
    siguiente = np.zeros(dimensiones,dtype = int)
    for i in range(ciclos):
        for f in range(m):
            for c in range(n):
                cantidad = vecinos(f, c)


    return siguiente

if __name__ == '__main__':
    limpia_pantalla()
    tablero, ciclos = leer_datos('datos.txt')
    mostrar_tablero(tablero, 'Inicial')
    tablero_final = ciclo_evolutivo(tablero, ciclos)
    mostrar_tablero(tablero_final, 'Final')
