salarioBase = 250000
venta = 50000
comision = 0.05

vendedor=int(input("Ingrese el id de vendedor: "))
cantidadDeVentas = int(input("Ingrese la cantidad mensual de ventas del vendedor " + str(vendedor)+ ": "))
dineroTotalPorVentas = float(input("Ingrese el monto total de las ventas realizadas: "))
salarioFinal = cantidadDeVentas * venta + dineroTotalPorVentas * comision + salarioBase

print("El vendedor", str(vendedor),"ha ganado este mes", salarioFinal)