import random
import os

def cadena_al_azar(n):
    adn = ''
    for i in range(n):
        adn = adn + random.choice('atcg')
    return adn

def complementaria(adn):
    adn1 = ''
    for i in range(len(adn)):
        if adn[i] == 'a':
            adn1 = adn1 + 't'
        elif adn[i] == 't':
            adn1 = adn1 + 'a'
        elif adn[i] == 'c':
            adn1 = adn1 + 'g'
        else:
            adn1 = adn1 + 'c'
    return adn1 

def muestra_cadenas(adn, adn1):
    print('Cadena original: ')
    print('               ',adn)
    print('Cadena Complementaria: ')
    print('               ',adn1)

def limpiar_pantalla():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

if __name__ == '__main__':
    limpiar_pantalla()
    n = int(input('Cantidad de proteinas: '))
    adn = cadena_al_azar(n)
    adn1 = complementaria(adn)
    muestra_cadenas(adn, adn1)

