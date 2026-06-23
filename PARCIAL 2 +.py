"""TP 2do parcial"""

def crearListaDeCamiones():
    listaId = int(input("Ingrese el id del camion: "))
    listaTiempoRecorrido = int(input("Ingrese el tiempo recorrido en el viaje: "))
    listaDistanciaRecorrida = int(input("Ingrese la distancia en kilometros enteros del viaje: "))
    listaCargaTotal = int(input("Ingrese la carga total en toneladas: "))
    return listaId, listaTiempoRecorrido, listaDistanciaRecorrida, listaCargaTotal


print(crearListaDeCamiones())