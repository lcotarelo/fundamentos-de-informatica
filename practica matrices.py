import random
# lista = []

# def buscarNumero(lista, numero):
#     i = 0
#     while i<len(lista) and lista[i] != numero:
#         i = i + 1
#     if i < len(lista):
#         return i
#     else: 
#         return -1
#     # for i in range(len(lista)):
#     #     if lista[i]!=numero:
#     #         i = i+1
#     #         if i == len(lista) and i != numero:
#     #             print("El numero no fue agregado")
#     #     else:
#     #         print("se encontro en la posicion ", i)

# cantidad = int(input("Cuantos numeros queres agregar: "))
# for i in range(cantidad):
#     lista.append(random.randint(1,6))

# numero = int(input("Que numeros queres buscar: "))

# posicion = buscarNumero(lista, numero)
# if posicion > 0: 
#     print("El numero esta en la posicion ", posicion)
# else:
#     print("El numero no esta")
# print(lista)

# metodo de seleccion
# lista = []
# def llenarLista():
#     for i in range(10):
#         lista.append(random.randint(1,1900))
#  
# def metodoSeleccion(lista):
#     largo = len(lista)
#     for i in range(largo-1):
#         for j in range(i+1, largo):
#             actual = lista[i]
#             siguiente = lista[j]
#             if actual > siguiente:
#                 actual = siguiente
#                 siguiente = actual
# print(lista)
# print(metodoSeleccion(lista))

matriz = []
F = random.randint(3,9)
C = random.randint(3,9)
for i in range(F):
    fila = []
    for c in range(C):
        numero = random.randint(1,3)
        fila.append(numero)
    matriz.append(fila)

print("F", F)
print("C", C)
for fila in matriz:
    print(fila)

buscarFila = int(input("ingrese la coordenada fila: "))
while buscarFila < 0 or buscarFila > F-1 :
    print("fuera de rango")
    buscarFila = int(input("ingrese la coordenada fila: "))
buscarColumna = int(input("ingrese la coordenada columna: "))
while buscarColumna < 0 or buscarColumna > C-1 :
    print("fuera de rango")
    buscarColumna = int(input("ingrese la coordenada columna: "))

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] % 2:
            matriz[i][j] = "O"
        else:
            matriz[i][j] = "X"
for fila in matriz:
    print(fila)

if matriz[buscarFila][buscarColumna] == "O":
    matriz[buscarFila][buscarColumna] = "M"
    print("Ganaste")
else:
    matriz[buscarFila][buscarColumna] = "W"
    print("Perdiste")
