"""BURBUJEO"""
import random
 
def burbujeo(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-i-1):
            if lista[j]>lista[j+1]:
                aux = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = aux
    return lista

a = burbujeo([43,342,12334,53,4,5,6,723,1,0])

print(a)