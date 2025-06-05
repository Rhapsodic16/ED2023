from collections import deque
import random

Cola = deque(["Marisol", "Pedro","Andrea", "Antonio", "Aram"])

#Remover
Cola.popleft()
print(Cola)

#Agregar.
Cola.append("Paola")
print(Cola)

#Recorrido.
for Persona in Cola:
    print(Persona)

#Ordenar
def bubble_sort(stack):
    n = len(stack)

    for i in range(n):

        for j in range(0, n-i-1):

            if stack[j] > stack[j+1]:

                stack[j], stack[j+1] = stack[j+1], stack[j]

    return stack

print("Stack antes de la ordenación: ", Cola)

bubble_sort(Cola)

print("Stack después de la ordenación: ", Cola)

#Mezclar.
random.shuffle(Cola)
print(Cola)

#