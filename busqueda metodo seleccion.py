def ordenamiento_seleccion(lista):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i]>lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

numeros = [3,9,1,7,999]
numeros = ordenamiento_seleccion(numeros)
print(numeros)