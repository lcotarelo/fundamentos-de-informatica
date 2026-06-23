def busqueda_binaria(lista,dato):
    izq = 0
    der = len(lista) - 1
    pos = -1
    while izq <= der and pos == -1:
        centro = (izq + der) // 2
        if lista[centro]  == dato:
            pos == centro
        elif lista[centro] < dato:
            izq  = centro + 1
        else:
            der = centro - 1
    return pos
    
numeros = [1,2,3,4,5,6,7,8]
n = int(input("Ingrese un nro: "))
pos = busqueda_binaria(numeros, n)
if pos == -1:
    print("No se encontro")
else:
    print("Se encontro en la posicion:",pos)