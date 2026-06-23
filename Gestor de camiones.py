HORAS = "H"
DIAS = "D"
STRING_VACIO = ""
ESPACIO = " "
KILOMETRAJE_MINIMO_PARA_REVISION_TECNICA = 20000
KILOMETROS = " km"
TONELADAS = " Tn"
ANCHO_DE_COLUMNA = 21
ENCABEZADO_DE_LISTADO = "       CAMION           TIEMPO PROMEDIO    DISTANCIA RECORRIDA      CARGA TOTAL"
ALERTA_DE_IDCAMION_INVALIDO = "Numero incorrecto, por favor, ingresar un camion con un numero valido (entero positivo) : "
MENSAJE_REVISION_MECANICA = "Revisión mecánica"
INGRESAR_ID_CAMION = "Por favor, ingresar el numero de camion: "
INGRESAR_TIEMPO_DE_USO = "Por favor, ingresar el tiempo de uso del camion en horas: "
INGRESAR_DISTANCIA_RECORRIDA = "Por favor, ingresar la distancia recorrida del camion en kilometros: "
SEPARADOR = "---------------------------------------------------------------------------------------------"
INGRESAR_CARGA_TRANSPORTADA = "Por favor, ingresar la carga transportada del camion en toneladas: "

def contarDigitos(numero):
  contador=0
  if numero<0:
    numero=numero*-1
    contador=1  
  while numero>0:
    contador+=1
    numero=numero//10
  return contador

def printNEspacios(cantidad):
  for i in range(cantidad):
    print(ESPACIO,end=STRING_VACIO)

def printCentradoNumText(numero,texto,espacioMaximo):
  largoTotal=contarDigitos(numero)+len(texto)
  if largoTotal>=espacioMaximo:
    print(numero,end=STRING_VACIO )
    print(texto,end=STRING_VACIO)
    return
  espaciosBlanco=espacioMaximo-largoTotal
  printNEspacios(espaciosBlanco//2)
  print(numero,end=STRING_VACIO)
  print(texto,end=STRING_VACIO)
  printNEspacios(espaciosBlanco-espaciosBlanco//2)

def printTiempoCentrado(dias,horas,espacioMaximo):
  if dias==0 and horas==0:
    printCentradoNumText(0,HORAS,espacioMaximo)
    return
  if dias==0:
    printCentradoNumText(horas,HORAS,espacioMaximo)
    return
  if horas==0:
    printCentradoNumText(dias,DIAS,espacioMaximo)
    return
  largoTotal=contarDigitos(dias)+contarDigitos(horas)+3
  if largoTotal>=espacioMaximo:
    print(dias,end=STRING_VACIO)
    print(DIAS,horas,end=STRING_VACIO)
    print(HORAS,end=STRING_VACIO)
    return
  espaciosBlanco=espacioMaximo-largoTotal
  printNEspacios(espaciosBlanco//2)
  print(dias,end=STRING_VACIO)
  print(DIAS,horas,end=STRING_VACIO)
  print(HORAS,end=STRING_VACIO)
  printNEspacios(espaciosBlanco-espaciosBlanco//2)

def intercambiarElementos(lista, posicion):
    aux = lista[posicion + 1]
    lista[posicion + 1] = lista[posicion]
    lista[posicion] = aux

def ordenarLista(idCamion, tiempoDeUsoDeCamion, distanciaTotalRecorrida, cargaCamion, cantidadDeViajes):
    for i in range(len(idCamion)):
        for j in range(len(idCamion) - i - 1):
            if cargaCamion[j] > cargaCamion[j + 1]:
                intercambiarElementos(cargaCamion, j)
                intercambiarElementos(idCamion, j)
                intercambiarElementos(tiempoDeUsoDeCamion, j)
                intercambiarElementos(distanciaTotalRecorrida, j)
                intercambiarElementos(cantidadDeViajes, j)
                
    return idCamion, tiempoDeUsoDeCamion, distanciaTotalRecorrida, cargaCamion, cantidadDeViajes

def funcPromedio(tieDeUnCamion,cantidadDeViajesDeUnCamion):
  promedio=tieDeUnCamion//cantidadDeViajesDeUnCamion
  return promedio//24,promedio%24   
    
def listar(idCamion,tiempoDeUsoDeCamion,distanciaTotalRecorrida,cargaCamion,cantidadDeViajes,idIngresado,tiempoIngresado,distanciaIngresada,cargaIngresada):
  for i in range(len(idCamion)):
    if idIngresado==idCamion[i]:
      tiempoDeUsoDeCamion[i]=tiempoDeUsoDeCamion[i]+tiempoIngresado
      distanciaTotalRecorrida[i]=distanciaTotalRecorrida[i]+distanciaIngresada
      cargaCamion[i]=cargaCamion[i]+cargaIngresada
      cantidadDeViajes[i]=cantidadDeViajes[i]+1
      return idCamion,tiempoDeUsoDeCamion,distanciaTotalRecorrida,cargaCamion,cantidadDeViajes
  idCamion.append(idIngresado)
  tiempoDeUsoDeCamion.append(tiempoIngresado)
  distanciaTotalRecorrida.append(distanciaIngresada)
  cargaCamion.append(cargaIngresada)
  cantidadDeViajes.append(1)
          
  return idCamion,tiempoDeUsoDeCamion,distanciaTotalRecorrida,cargaCamion,cantidadDeViajes

def confirmarIngreso(idIngresado, tiempoIngresado, distanciaIngresada, cargaIngresada):
    print("Va a agregar el siguiente reporte:")
    print("ID el camion:", idIngresado)
    print("Tiempo de uso:", tiempoIngresado)
    print("Distancia recorrida:", distanciaIngresada)
    print("Carga:", cargaIngresada)
    agrega = input("Ingrese S para aceptar u otra tecla para descartar el ingreso: ")
    if agrega == "S" or agrega == "SI" or agrega == "s" or agrega == "si" or agrega == "sI" or agrega == "Si":
      listaDeCamiones = listar(idCamion, tiempoDeUsoDeCamion, distanciaTotalRecorrida, cargaCamion, cantidadDeViajes, idIngresado, tiempoIngresado, distanciaIngresada, cargaIngresada)    
      print("El reporte actual fue agregado.")
    else:
      print("El reporte actual no ha sido agregado.")

def imprimirListado(printCentradoNumText, printTiempoCentrado, funcPromedio, STRING_VACIO, KILOMETRAJE_MINIMO_PARA_REVISION_TECNICA, KILOMETROS, TONELADAS, ANCHO_DE_COLUMNA, MENSAJE_REVISION_MECANICA, idCamion, tiempoDeUsoDeCamion, distanciaTotalRecorrida, cargaCamion, cantidadDeViajes):
    print(ENCABEZADO_DE_LISTADO)
    for i in range(len(idCamion)):
      printCentradoNumText(idCamion[i],STRING_VACIO,ANCHO_DE_COLUMNA)
      dias,horas=funcPromedio(tiempoDeUsoDeCamion[i],cantidadDeViajes[i])
      printTiempoCentrado(dias,horas,ANCHO_DE_COLUMNA)
      printCentradoNumText(distanciaTotalRecorrida[i],KILOMETROS,ANCHO_DE_COLUMNA)
      printCentradoNumText(cargaCamion[i],TONELADAS,ANCHO_DE_COLUMNA)
      if distanciaTotalRecorrida[i]>KILOMETRAJE_MINIMO_PARA_REVISION_TECNICA:
        print(MENSAJE_REVISION_MECANICA)
      print()


idCamion=[]
tiempoDeUsoDeCamion=[]
distanciaTotalRecorrida=[]
cargaCamion=[]
cantidadDeViajes=[]

idIngresado=int(input(INGRESAR_ID_CAMION))

while idIngresado<=0: 
  idIngresado=int(input(ALERTA_DE_IDCAMION_INVALIDO)) 

while idIngresado != -1 :
  tiempoIngresado=int(input(INGRESAR_TIEMPO_DE_USO))
  distanciaIngresada=int(input(INGRESAR_DISTANCIA_RECORRIDA))
  cargaIngresada=int(input(INGRESAR_CARGA_TRANSPORTADA))
  confirmarIngreso(idIngresado, tiempoIngresado, distanciaIngresada, cargaIngresada)
  print(ESPACIO)
  idIngresado=int(input(INGRESAR_ID_CAMION))
  while idIngresado < -1 or idIngresado==0:
    idIngresado=int(input()) 

idCamion,tiempoDeUsoDeCamion,distanciaTotalRecorrida,cargaCamion,cantidadDeViajes=ordenarLista(idCamion,tiempoDeUsoDeCamion,distanciaTotalRecorrida,cargaCamion,cantidadDeViajes)

print(SEPARADOR)

imprimirListado(printCentradoNumText, printTiempoCentrado, funcPromedio, STRING_VACIO, KILOMETRAJE_MINIMO_PARA_REVISION_TECNICA, KILOMETROS, TONELADAS, ANCHO_DE_COLUMNA, MENSAJE_REVISION_MECANICA, idCamion, tiempoDeUsoDeCamion, distanciaTotalRecorrida, cargaCamion, cantidadDeViajes)