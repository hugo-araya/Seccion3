''' Juego del Gato
    Creado por : Hugo Araya Carrasco
    Fecha: 04 Octubre 2022
    Version: 1.2
'''
import random

def lanzar_dado():
    return random.randint(1,6)

def elige(humano, computador):
    if humano > computador:
        jugador1 = 'H'
    else:
        jugador1 = 'C'
    return jugador1

def comienza(us1, us2):
    humano = 0
    computador = 0
    while humano == computador:
        humano = lanzar_dado()
        computador = lanzar_dado()
    jugador1 = elige(humano, computador)
    return jugador1

# Solo incorpora el lanzamiento del dado y la seleccion del mayor.

if __name__=='__main__':
    jugador1 = comienza('Humano', 'Computador')
    print ('Comienza el juego: ', jugador1)