"""EXPENSAS"""
depaexpensabaja = 0
depaexpensamedia = 0
depaexpensaalta = 0
mayorexpensa = 0
expensas = 0
maximo = expensas
cantidaddepa = 0
expensas = int(input("Ingrese expensas del mes: "))
while expensas >=0:
    if expensas > maximo:
        maximo = expensas
    if expensas > 0 and expensas < 150000:
        depaexpensabaja = depaexpensabaja + 1
    elif expensas >= 150000 and expensas <= 450000:
        depaexpensamedia = depaexpensamedia + 1
    else:
        depaexpensaalta = depaexpensaalta + 1
    cantidaddepa = cantidaddepa + 1
    expensas = int(input("Ingrese expensas del mes: "))
print(depaexpensabaja/cantidaddepa*100)
print(depaexpensamedia/cantidaddepa*100)
print(depaexpensaalta/cantidaddepa*100)
print("La expensa mas cara es:", maximo)
print("FIN")
