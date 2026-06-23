"""Generar un algoritmo que permita obtener el promedio de las notas de un curso de programación,
el porcentaje de aprobados y el porcentaje de desaprobados. 
Para ello se ingresarán 20 notas y luego se mostrarán los resultados. 
Validar que las notas ingresadas no sean menores a 1 ni mayores a 10"""

cantidadnotas = 4
contador = 0
aprobados = 0
sumaaprobados = 0
desaprobados = 0
sumadesaprobados = 0
while contador < cantidadnotas:
    nota = float(input("Ingrese una nota: "))
    while nota <=1 or nota > 10:
        print("Error. Las notas deben ser mayor a 1 y menores o igual que 10")
        nota = float(input("Ingrese una nota"))
    if nota > 4 :
        sumaaprobados = sumaaprobados + 1
        
    else :
        sumadesaprobados = sumadesaprobados + 1
    contador = contador + 1 
print("Cantidad aprobados:", sumaaprobados, ", correspondiendo al",sumaaprobados/cantidadnotas*100  ,"%")
print("Cantidad desaprobados:", sumadesaprobados, ", correspondiendo al",sumadesaprobados/cantidadnotas*100  ,"%")
                     