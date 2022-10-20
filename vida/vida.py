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
    dimensiones=(m+2,n+2)
    tablero = np.zeros(dimensiones,dtype = int)
    for linea in ent:
        linea = linea.rstrip('\n')
        lista = linea.split(' ')
        tablero[int(lista[0])+1][int(lista[1])+1]=1  
    return tablero

def leer_datos(nombre):
    ent = open(nombre)
    linea = ent.readline().rstrip('\n')
    m, n, k, l = devuelve_variables(linea)
    tablero = devuelve_tablero(ent, m, n)
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

def vecinos(tablero, f, c):
    v = tablero[f-1][c-1]
    v = v + tablero[f-1][c]
    v = v + tablero[f-1][c+1]
    v = v + tablero[f][c-1]
    v = v + tablero[f][c+1]
    v = v + tablero[f+1][c-1]
    v = v + tablero[f+1][c]
    v = v + tablero[f+1][c+1]
    return v

def _muestra_vecinos(f, c, cantidad):
    print(f,c,cantidad)

def ciclo_evolutivo(tablero, ciclos):
    fc = tablero.shape
    m = int(fc[0])
    n = int(fc[1])
    dimensiones=(m,n)
    siguiente = np.zeros(dimensiones,dtype = int)
    for i in range(ciclos):
        for f in range(1, m-1):
            for c in range(1, n-1):
                cantidad = vecinos(tablero, f, c)
                if tablero[f][c] == 0:
                    if cantidad > 1 and cantidad < 4:
                        siguiente[f][c] = 1
                else:
                    if cantidad > 1 and cantidad < 4:
                        siguiente[f][c] = 1

    return siguiente

if __name__ == '__main__':
    limpia_pantalla()
    tablero, ciclos = leer_datos('datos.txt')
    mostrar_tablero(tablero, 'Inicial')
    tablero_final = ciclo_evolutivo(tablero, ciclos)
    mostrar_tablero(tablero_final, 'Final')
