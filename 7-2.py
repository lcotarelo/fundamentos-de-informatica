"""
Escribir una función para ingresar desde el teclado una serie de números entre A
y B y guardarlos en una lista. En caso de ingresar un valor fuera de rango la
función mostrará un mensaje de error y solicitará un nuevo número. Para finalizar la
carga se deberá ingresar -1. La función recibe como parámetros los valores de A
y B, y devuelve la lista cargada (o vacía, si el usuario no ingresó nada) como
valor de retorno. Tener en cuenta que A puede ser mayor, menor o igual a B"""

def ingresarporteclado(a,b):
    lista = []
    numero = int(input("Ingrese un numero menos a 10 y mayor a 0. para salir ingrese -1: "))
    while numero != -1:
        if numero>a and numero<b or numero>b and numero<a :
            lista.append(numero)
            numero = int(input("Ingrese un numero menos a 10 y mayor a 0. para salir ingrese -1: "))
        else:
            print("Error")
            numero = int(input("Ingrese un numero menos a 10 y mayor a 0. para salir ingrese -1: "))
    return lista

""" 2 - Calcular la suma de los números de la lista"""

# def sumaLista(lista):
#     suma = 0
#     for i in range(len(lista)):
#         suma = suma + lista[i]
#     return suma
# 
# lista = ingresarporteclado(1,30)
# 
# print(lista)
# 
# print(sumaLista([3, 5, 2]))

# Escribir una función para contar cuántas veces aparece un valor dentro de la lista.
# La función recibe como parámetros la lista y el valor a buscar, y devuelve un número entero.

def cuantasveces(lista, numero):
    veces = 0
    for i in range(len(lista)):
        if numero == lista[i]:
            veces = veces + 1
    return veces

print(cuantasveces([2,4,9,9,2,4,10,9,6,1,10,8,4,10],9))