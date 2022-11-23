import random
def aleatorio(cantidad):
    sal = open('z_aleatorio1.txt','w')
    for i in range(cantidad):
        numero = random.randint(0, 999999)
        sal.write(str(numero)+'\n')
    sal.close()

def ordenado(cantidad):
    sal = open('z_ordenado1.txt','w')
    for i in range(cantidad):
        sal.write(str(i)+'\n')
    sal.close()   

def inverso(cantidad):
    sal = open('z_inverso1.txt','w')
    for i in range(cantidad, 0, -1):
        sal.write(str(i)+'\n')
    sal.close()   

if __name__ == '__main__':
    cantidad = int(input('Cantidad de elementos a generar para el archivo: '))
    aleatorio(cantidad)
    ordenado(cantidad)
    inverso(cantidad)