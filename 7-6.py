"""Escribir una función para devolver una lista con todas las posiciones que ocupa
un valor pasado como parámetro, utilizando búsqueda secuencial en una lista
desordenada. La función debe devolver una lista vacía si el elemento no se
encuentra en la lista original."""

def busqueda_secuencial(lista, n):
    listarepetidos = []
    for i in range(len(lista)):
        if(lista[i] == n):
            listarepetidos.append(i)
    return listarepetidos
numeros = [3,2,3,8,1,3]
n = int(input("Ingrese un nro a buscar: "))
listarepetidos = busqueda_secuencial(numeros, n)
print(listarepetidos)