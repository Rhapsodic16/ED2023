#Método burbuja.
def MetodoBurbuja(lista):
    longitud = len(lista)

    for i in range(longitud):
        for j in range(0, longitud-i-1):
            if lista[j] > lista[j+1] :
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

lista = ['u', 'o', 'i', 'e', 'a']

print(MetodoBurbuja(lista))

#Por selección.
def OrdenamientoSeleccion(lista):
    for i in range(len(lista)):
        IndiceMinimo = i
        for j in range(i+1, len(lista)):
            if lista[j]< lista[IndiceMinimo]:
                IndiceMinimo = j
        lista[i], lista[IndiceMinimo] = lista[IndiceMinimo], lista[i]

    return lista

lista = [22, 32, 11, 54, 78, 5, 34]

print(OrdenamientoSeleccion(lista))

#Por inserción.
def OrdenamientoInsercion(lista):
    for i in range(1, len(lista)):
        LlaveItem = lista[i]
        j = i-1
        while j>= 0 and LlaveItem<lista[j]:
            lista[j+1] = lista[j]
            j-=1
        lista[j+1]= LlaveItem
    return lista


lista = [22, 32, 11, 54, 78, 5, 34]

print(OrdenamientoInsercion(lista)) 