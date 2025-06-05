import random

Lista=[3,52,6,7,8]
print(Lista)

#Incersión
Lista.insert(4,0)
print(Lista)

#Recorrido
for X in Lista:
    print(X)

#Búsqueda
# Declarar la lista estática

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Elemento a buscar

search_item = 10

# Buscar el elemento en la lista

if search_item in numbers:

    print(f'{search_item} se encuentra en la lista.')

else:

    print(f'{search_item} no se encuentra en la lista.')

#Eliminación
Numero = int(input("Ingrese el número que desee eliminación: "))
Lista.remove(Numero)
print(Lista)

#Ordenación
Lista.sort()
print(Lista)

#Mezclar
random.shuffle(Lista)