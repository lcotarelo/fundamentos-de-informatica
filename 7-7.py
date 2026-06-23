 """Ídem anterior, utilizando búsqueda
binaria sobre una lista ordenada"""
 
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