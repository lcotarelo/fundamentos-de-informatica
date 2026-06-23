import random
def cargar_lista():
    lista = []
    for i in range(4):
        n = random.randint(-5,20)
        lista.append(n)
    return lista

lista1 = cargar_lista()
lista2 = cargar_lista()

print(lista1)
print(lista2)