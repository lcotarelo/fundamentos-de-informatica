"METODO DE INSERCION"

def insercion(lista):
    for i in range(1, len(lista)):
        aux = lista[i]
        j = i
        while j>0 and lista[i-1]>aux:
            lista[j] = lista[j-1]
            j= j-1
        lista[j] = aux
    return lista

a = [212,23,45,365436,1,7578,5684,3463,23,34,121]
print(insercion(a))