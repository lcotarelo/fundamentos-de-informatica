def esmultiplo(numero1, numero2):
    if(numero1%numero2 == 0):
        return True
    return False


numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
resultado = esmultiplo(numero1,numero2)
print(resultado)