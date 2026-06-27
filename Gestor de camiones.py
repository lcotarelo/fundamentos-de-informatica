UNIDAD_HORAS = "H"
UNIDAD_DIAS = "D"
KILOMETRAJE_MINIMO_PARA_REVISION_TECNICA = 20000
UNIDAD_DISTANCIA = " km"
UNIDAD_CARGA = " Tn"
ANCHO_DE_COLUMNA = 21
ENCABEZADO_DE_LISTADO = "       CAMION           TIEMPO PROMEDIO    DISTANCIA RECORRIDA      CARGA TOTAL"
ALERTA_DE_ID_CAMION_INVALIDO = "Numero incorrecto, por favor, ingresar un camion con un numero valido (entero positivo) : "
MENSAJE_REVISION_MECANICA = "Revisión mecánica"
INGRESAR_ID_CAMION = "Por favor, ingresar el numero de camion: "
INGRESAR_TIEMPO_DE_USO = "Por favor, ingresar el tiempo de uso del camion en horas: "
INGRESAR_DISTANCIA_RECORRIDA = "Por favor, ingresar la distancia recorrida del camion en kilometros: "
SEPARADOR = "---------------------------------------------------------------------------------------------"
INGRESAR_CARGA_TRANSPORTADA = "Por favor, ingresar la carga transportada del camion en toneladas: "
CONFIRMACION_AGREGAR = "Va a agregar el siguiente reporte: "
CONFIRMACION_ID_CAMION = "ID el camion:"
CONFIRMACION_TIEMPO_DE_USO = "Tiempo de uso:"
CONFIRMACION_DISTANCIA_RECORRIDA = "Distancia recorrida:"
CONFIRMACINO_CARGA = "Carga:"
CONFIRMACION_INGRESO = "Ingrese S para aceptar u otra tecla para descartar el ingreso: "
CONFIRMACION_REPORTE_CREADO = "El reporte actual fue agregado."
CONFIRMACION_REPORTE_RECHAZADO = "El reporte actual no fue agregado."
 
idCamion=[]
tiempoDeUsoDeCamion=[]
distanciaTotalRecorrida=[]
cargaCamion=[]
cantidadDeViajes=[]
 
 #mate
def contarDigitos(numero):
    contador=0
    if numero<0:
        numero=numero*-1
        contador=1  
    while numero>0:
        contador+=1
        numero=numero//10
    return contador

 # leandro
def printNEspacios(cantidad):
    for i in range(cantidad):
      print(" ",end="")
 
 #mate
def printCentradoNumText(numero,texto,espacioMaximo):
    largoTotal=contarDigitos(numero)+len(texto)
    if largoTotal>=espacioMaximo:
        print(numero,end="" )
        print(texto,end="")
        return
    espaciosBlanco=espacioMaximo-largoTotal
    printNEspacios(espaciosBlanco//2)
    print(numero,end="")
    print(texto,end="")
    printNEspacios(espaciosBlanco-espaciosBlanco//2)
 
 #leandro
def printTiempoCentrado(dias,horas,espacioMaximo):
    if dias==0 and horas==0:
        printCentradoNumText(0,UNIDAD_HORAS,espacioMaximo)
        return
    if dias==0:
        printCentradoNumText(horas,UNIDAD_HORAS,espacioMaximo)
        return
    if horas==0:
        printCentradoNumText(dias,UNIDAD_DIAS,espacioMaximo)
        return
    largoTotal=contarDigitos(dias)+contarDigitos(horas)+3
    if largoTotal>=espacioMaximo:
        print(dias,end="")
        print(UNIDAD_DIAS,horas,end="")
        print(UNIDAD_HORAS,end="")
        return
    espaciosBlanco=espacioMaximo-largoTotal
    printNEspacios(espaciosBlanco//2)
    print(dias,end="")
    print(UNIDAD_DIAS,horas,end="")
    print(UNIDAD_HORAS,end="")
    printNEspacios(espaciosBlanco-espaciosBlanco//2)
 
 #mate
def validarEntradaPositiva(texto):
    valor=int(input(texto))
    while valor<=0:
        valor=int(input(texto))
    return valor
  
  # TOBY 
def intercambiarElementos(lista, posicion):
    aux = lista[posicion + 1]
    lista[posicion + 1] = lista[posicion]
    lista[posicion] = aux
 
 #toby
def mover(listas,posicion):
  for i in range(len(listas)):
    intercambiarElementos(listas[i],posicion)
 
#toby
def ordenarLista():
    for i in range(len(idCamion)):
        for j in range(len(idCamion) - i - 1):
            if cargaCamion[j] > cargaCamion[j + 1]:
              mover([idCamion, tiempoDeUsoDeCamion, distanciaTotalRecorrida, cargaCamion, cantidadDeViajes],j)
 
 #leandro
def crearTiempoPromedio(tiempoDeUnCamion,cantidadDeViajesDeUnCamion):
    promedio=tiempoDeUnCamion//cantidadDeViajesDeUnCamion
    return promedio//24,promedio%24
 
 #santi
def listar(idIngresado, tiempoIngresado,distanciaIngresada,cargaIngresada):
    for i in range(len(idCamion)):
        if idIngresado==idCamion[i]:
            tiempoDeUsoDeCamion[i]=tiempoDeUsoDeCamion[i]+tiempoIngresado
            distanciaTotalRecorrida[i]=distanciaTotalRecorrida[i]+distanciaIngresada
            cargaCamion[i]=cargaCamion[i]+cargaIngresada
            cantidadDeViajes[i]=cantidadDeViajes[i]+1
            return
    idCamion.append(idIngresado)
    tiempoDeUsoDeCamion.append(tiempoIngresado)
    distanciaTotalRecorrida.append(distanciaIngresada)
    cargaCamion.append(cargaIngresada)
    cantidadDeViajes.append(1)
 
 #santi
def confirmarIngreso(idIngresado, tiempoIngresado, distanciaIngresada, cargaIngresada):
    print(CONFIRMACION_AGREGAR)
    print(CONFIRMACION_ID_CAMION, idIngresado)
    print(CONFIRMACION_TIEMPO_DE_USO, tiempoIngresado)
    print(CONFIRMACION_DISTANCIA_RECORRIDA, distanciaIngresada)
    print(CONFIRMACINO_CARGA, cargaIngresada)
    agrega = input(CONFIRMACION_INGRESO)
    if agrega == "S" or agrega == "SI" or agrega == "s" or agrega == "si" or agrega == "sI" or agrega == "Si":
      listar(idIngresado, tiempoIngresado, distanciaIngresada, cargaIngresada)    
      print(CONFIRMACION_REPORTE_CREADO)
    else:
      print(CONFIRMACION_REPORTE_RECHAZADO)
 
 #Manu
def imprimirReporte():
    for i in range(len(idCamion)):
      printCentradoNumText(idCamion[i],"",ANCHO_DE_COLUMNA)
      dias,horas=crearTiempoPromedio(tiempoDeUsoDeCamion[i],cantidadDeViajes[i])
      printTiempoCentrado(dias,horas,ANCHO_DE_COLUMNA)
      printCentradoNumText(distanciaTotalRecorrida[i],UNIDAD_DISTANCIA,ANCHO_DE_COLUMNA)
      printCentradoNumText(cargaCamion[i],UNIDAD_CARGA,ANCHO_DE_COLUMNA)
      if distanciaTotalRecorrida[i]>KILOMETRAJE_MINIMO_PARA_REVISION_TECNICA:
        print(MENSAJE_REVISION_MECANICA)
      print()
 
idIngresado=validarEntradaPositiva(INGRESAR_ID_CAMION)
 
while idIngresado != -1 :
  tiempoIngresado=validarEntradaPositiva(INGRESAR_TIEMPO_DE_USO)
  distanciaIngresada=validarEntradaPositiva(INGRESAR_DISTANCIA_RECORRIDA)
  cargaIngresada=validarEntradaPositiva(INGRESAR_CARGA_TRANSPORTADA)
  confirmarIngreso(idIngresado, tiempoIngresado, distanciaIngresada, cargaIngresada)
  print(SEPARADOR)
  idIngresado=int(input(INGRESAR_ID_CAMION))
  while idIngresado < -1 or idIngresado==0:
    idIngresado=int(input(ALERTA_DE_ID_CAMION_INVALIDO))
 
ordenarLista()
 
print(ENCABEZADO_DE_LISTADO)
 
imprimirReporte()