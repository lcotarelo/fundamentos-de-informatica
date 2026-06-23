"""Solicitar al usuario que ingrese la temperatura que hizo en Ushuaia
durante los días del mes de julio del 2025, teniendo en cuenta que la
temperatura no debe ser mayor a 6° ni menor a -6°.
¿Cuál es el promedio de temperatura que hizo? 
Si la temperatura ingresada está fuera de rango, volver a solicitarla. """

diasDeJulio = 2
sumaTemperatura = 0
for i in range(diasDeJulio):
    temperatura = float(input("Ingrese la temperatura "))
    while temperatura < -6 or temperatura > 6:
        print("Error. La temperatura debe ser mayor a -6 y menor a 6")
        temperatura = float(input("Ingrese la temperatura "))
    sumaTemperatura = sumaTemperatura + temperatura
print("Promedio ", sumaTemperatura/diasDeJulio)
        

    