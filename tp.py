def contarDigitos(numero):
  contador=0
  if numero<=0:
    numero=numero*-1
    contador=1  #para el -
  while numero>0:
    contador+=1
    numero=numero//10
  return contador

def printNEspacios(cantidad):
  for _ in range(cantidad):
    print(" ",end="")

def printCentradoNumText(numero,texto,espacioMaximo):
  largoTotal=contarDigitos(numero)+len(texto)
  if largoTotal>=espacioMaximo:
    print(numero,end="")
    print(texto,end="")
    return
  espaciosBlanco=espacioMaximo-largoTotal
  printNEspacios(espaciosBlanco//2)
  print(numero,end="")
  print(texto,end="")
  printNEspacios(espaciosBlanco-espaciosBlanco//2)

def printTiempoCentrado(dias,horas,espacioMaximo):
  if dias==0 and horas==0:
    printCentradoNumText(0,"H",espacioMaximo)
    return
  if dias<=0:
    printCentradoNumText(horas,"H",espacioMaximo)
    return
  if horas<=0:
    printCentradoNumText(dias,"D",espacioMaximo)
    return
  largoTotal=contarDigitos(dias)+contarDigitos(horas)+3
  if largoTotal>=espacioMaximo:
    print(dias,end="")
    print("D",horas,end="")
    print("H",end="")
    return
  espaciosBlanco=espacioMaximo-largoTotal
  printNEspacios(espaciosBlanco//2)
  print(dias,end="")
  print("D",horas,end="")
  print("H",end="")
  printNEspacios(espaciosBlanco-espaciosBlanco//2)



def burbujeo(idCamion,tiempoRecorrido,distanciaRecorrida,cargaTotal,cantidadDeViajes):
    for i in range(len(idCamion)):
        for j in range(len(idCamion)-i-1):
            if cargaTotal[j]>cargaTotal[j+1]:
                aux=cargaTotal[j+1]
                cargaTotal[j+1]=cargaTotal[j]
                cargaTotal[j]=aux

                aux=idCamion[j+1]
                idCamion[j+1]=idCamion[j]
                idCamion[j]=aux

                aux=tiempoRecorrido[j+1]
                tiempoRecorrido[j+1]=tiempoRecorrido[j]
                tiempoRecorrido[j]=aux

                aux=distanciaRecorrida[j+1]
                distanciaRecorrida[j+1]=distanciaRecorrida[j]
                distanciaRecorrida[j]=aux

                aux=cantidadDeViajes[j+1]
                cantidadDeViajes[j+1]=cantidadDeViajes[j]
                cantidadDeViajes[j]=aux
    return idCamion,tiempoRecorrido,distanciaRecorrida,cargaTotal,cantidadDeViajes



def crearMatriz(idCamion,tiempoRecorrido,distanciaRecorrida,cargaTotal):
    matriz=[]
    for i in range(len(idCamion)):
        matriz.append([idCamion[i],tiempoRecorrido[i],distanciaRecorrida[i],cargaTotal[i]])
    return matriz

       
    
def funcPromedio(tieDeUnCamion,cantidadDeViajesDeUnCamion):
  promedio=tieDeUnCamion//cantidadDeViajesDeUnCamion
  return promedio//24,promedio%24   #promedioDias,promedioHoras
    
def funcListado(idCamion,tiempoRecorrido,distanciaRecorrida,cargaTotal,cantidadDeViajes,idIng,tieIng,disIng,carIng):
    encontrado=False

    for i in range(len(idCamion)):
        if idIng==idCamion[i]:
            encontrado=True
            tiempoRecorrido[i]=tiempoRecorrido[i]+tieIng
            distanciaRecorrida[i]=distanciaRecorrida[i]+disIng
            cargaTotal[i]=cargaTotal[i]+carIng
            cantidadDeViajes[i]=cantidadDeViajes[i]+1
            
    if encontrado==False: 
        idCamion.append(idIng)
        tiempoRecorrido.append(tieIng)
        distanciaRecorrida.append(disIng)
        cargaTotal.append(carIng)
        cantidadDeViajes.append(1)
            
    return idCamion,tiempoRecorrido,distanciaRecorrida,cargaTotal,cantidadDeViajes



#Programa principal
idCamion=[]
tiempoRecorrido=[]
distanciaRecorrida=[]
cargaTotal=[]
cantidadDeViajes=[]

idIng=int(input("Por favor, ingresar numero de camion: "))

while idIng<0: #Validacion inicial para obligar que se ingrese un primer camion
    idIng=int(input("Numero incorrecto, porfavor, ingresar camion con un numero valido(entero positivo) : ")) 

while idIng != -1:
    tieIng=int(input("Por favor, ingresar tiempo empleado o recorrido del camion en horas: "))
    disIng=int(input("Por favor, ingresar distancia recorrida del camion en kilometros: "))
    carIng=int(input("Por favor, ingresar carga transportada del camion en toneladas: "))
    listaDeCamiones=funcListado(idCamion,tiempoRecorrido,distanciaRecorrida,cargaTotal,cantidadDeViajes,idIng,tieIng,disIng,carIng)
    print("---------------------------------------------------------------------------------------------")
    idIng=int(input("Por favor, ingresar numero de camion: "))
    while idIng < -1:
        idIng=int(input("Numero incorrecto. Por favor, ingresar camion con un numero valido (entero positivo): ")) 

    

idCamion,tiempoRecorrido,distanciaRecorrida,cargaTotal,cantidadDeViajes=burbujeo(idCamion,tiempoRecorrido,distanciaRecorrida,cargaTotal,cantidadDeViajes)
matriz=crearMatriz(idCamion,tiempoRecorrido,distanciaRecorrida,cargaTotal)

print("       CAMION           TIEMPO PROMEDIO    DISTANCIA RECORRIDA      CARGA TOTAL")
for i in range(len(idCamion)):
  printCentradoNumText(idCamion[i],"",21)
  dias,horas=funcPromedio(tiempoRecorrido[i],cantidadDeViajes[i])
  printTiempoCentrado(dias,horas,21)
  printCentradoNumText(distanciaRecorrida[i],"",21)
  printCentradoNumText(cargaTotal[i],"",21)
  print()
