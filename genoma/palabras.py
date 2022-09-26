import os
import requests

def lee_frase():
    return('Esto, es una frase. y no se que mas debo, poner en la frase eso es todo por hoy.')

def a_mayusculas(frase):
    return frase.upper()

def elimina_basura(frase):
    frase = frase.replace(',', '')
    frase = frase.replace('.', '')
#    frase = frase.replace('\t', '')
#    frase = frase.replace('\n', '')
    return frase

def crea_diccionario(lista):
    dic = {}
    for palabra in lista:
        if palabra in dic:
            dic[palabra] = dic[palabra]+1
        else:
            dic[palabra] = 1
    return dic
    
def muestra_diccionario(dic):
    print(dic)

def limpiar_pantalla():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

if __name__ == '__main__':
    limpiar_pantalla()
    frase = lee_frase()
#    res = requests.get('https://portal.ucm.cl')
#    frase = res.text
    frase = a_mayusculas(frase)
    frase = elimina_basura(frase)
    lista_palabras = frase.split(' ')
    dic_pal = crea_diccionario(lista_palabras)
    muestra_diccionario(dic_pal)