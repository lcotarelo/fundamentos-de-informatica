"""lista paralela"""

def ordenamiento(lista1, lista2, lista3):
    for i in range(len(lista1)):
        for j in range(len(lista1)-i-1):
            if lista1[j] > lista1[j+1]:
                aux = lista1[j]
                lista1[j] = lista1[j+1]
                lista1[j+1] = aux
                aux = lista2[j]
                lista2[j] = lista2[j+1]
                lista2[j+1] = aux
                aux = lista3[j]
                lista3[j] = lista3[j+1]
                lista3[j+1] = aux
    return lista1, lista2, lista3

lista1 = [14,10,4,12]
lista2 = ["COTARELO", "SCILETTA","MIRANDA","NADAL"]
lista3 = [9,6,10,8]

codigo, apellido, nota = ordenamiento(lista1, lista2, lista3)

print("CODIGO", codigo)
print("APELLIDO", apellido)
print("NOTA", nota)
