import random

def busqueda_lineal(lista, objetivo):
    busqueda = False
    for x in lista:
        if x == objetivo:
            busqueda = True
            break

    return busqueda

if __name__ == '__main__':
    objetivo = int(input("Que numero buscas? "))
    tamano = int(input("Cual es el tamaño de la lista "))
    lista = sorted([random.randint(1,100) for i in range(tamano)])
    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    if encontrado == True:
        print(f'El numero {objetivo} esta en la lista')
    elif encontrado == False:
        print(f'El numero {objetivo} no esta en la lista')