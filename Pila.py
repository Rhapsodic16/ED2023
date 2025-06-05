#Ejemplo de pilas estáticas en una escuela con la lista de alumnos.
Pila = [2, 56, 70, 800, 300, 76, 52]

#Dependencia 
import random

#Incersión.
Pila.append(98)
print(Pila)

#Recorrido.
for elemento in reversed(Pila[:]):
    print(elemento)

#Búsqueda.
Buscar = int(input("Escribe el elemento a buscar: "))
for i in range(len(Pila)-1, -1, -1):
    if Pila[i] == Buscar:
        print(f'Se encontró {Buscar}')
        break
else :
        print("No se encontró el elemento.")

#Eliminación.
Eliminar = int(input("Escribe el elemento que desea eliminar: "))
PilaAuxiliar = []
for i in range(len(Pila)-1, -1, -1):
    if Pila[i] != Eliminar:
        PilaAuxiliar.append(Pila[i])
    
Pila = PilaAuxiliar
print(Pila)

#Ordenación.
Longitud = len(Pila)
for i in range(Longitud):
     for j in  range(0,Longitud-i-1):
          if Pila[j] >Pila[j+1]:
               Pila[j], Pila[j+1] = Pila[j+1], Pila[j]
print(Pila)

#Mezcla.
PilaAleatoria = []    

while Pila:
    Elemento = random.choice(Pila)
    Pila.remove(Elemento)
    PilaAleatoria.append(Elemento)
    
Pila = PilaAleatoria

print(Pila)