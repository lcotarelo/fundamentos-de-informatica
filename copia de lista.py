def copiar_lista(lista1, lista2):
    for i in range(len(lista1)):
        lista2.append(lista1[i])
    return lista2

nume1=[2,4,9,6]
nume2=[]

nume2= copiar_lista(nume1, nume2)
print(nume2)