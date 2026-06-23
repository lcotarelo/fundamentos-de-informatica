def busqueda_secuencial(lista, n):
    for i in range(len(lista)):
        if(lista[i] == n):
            return i
    return -1
numeros = [9,2,7,8,1,5]
n = int(input("Ingrese un nro a buscar: "))
posicion = busqueda_secuencial(numeros, n)
print(posicion)