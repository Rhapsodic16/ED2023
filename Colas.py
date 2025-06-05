#Ejemplo de cola estáticas en la fila de un cine.
#Importamos random para pode mezclar la cola.
import random

#Importamos random para pode mezclar la cola.
from collections import deque

#Importamos os para poder limpiar la pantalla y tener un resultado más limpio.
import os

#Declaramos una cola de clientes como ejemplo.
Clientes = deque(['Diego', 'Ramiro', 'Patricio', 'Juan', 'Estefania', 'Alicia'])

#Función que muestra la entrada al programa.
def Entrada(Clientes):
    #Limpiamos la pantalla.
    os.system("cls")

    #Mostramos una pequeña presentación del programa.
    print("-----------------------------------------------------")
    print("           Bienvenido a la fila del cine.            ")
    print("-----------------------------------------------------")

    #Mostramos las opciones.
    Clientes = Opciones(Clientes) 

    #Retornamos la cola con las modificaciones.
    return Clientes

#Funcion que muestra las opciones del programa.
def Opciones(Clientes):
    #Mostramos las opciones.
    print("    Opciones para escoger:")
    print("1. Agregar cliente.")
    print("2. Buscar un cliente en la cola.")
    print("3. Mostrar la cola de clientes.")
    print("4. Eliminar cliente de la cola.")
    print("5. Ordenar cola alfabéticamente.")
    print("6. Mezclar cola.")
    print("7. Atender al cliente.")

    #Se selecciona una opción y se almacena en una variable para escoger la función a usar.
    Seleccion = int(input("Seleccione la opción que necesita con el número: "))
    
    #Creamos una nueva cola con los valores de la cola actual para poder modificarla.
    Fila = Clientes

    #El programa selecciona la ruta dependiendo de la seleccioón del usuario.
    if Seleccion == 1: #Inserta un cliente en la cola.
        #Llama a la función inserción y se almacena el resultado en la cola que vamos a modificar.
        Fila = Insercion(Fila)

        #Mostramos la cola en pantalla.
        print("\nLa cola actual es: ")
        Recorrer(Fila)
    elif Seleccion == 2:#Buscar a un cliente en la cola.
        #Llama a la función Buscar.
        Buscar(Fila)
    elif Seleccion == 3:#Recorre la cola de clientes y la muestra en pantalla.
        #Llama a la función Recorrer.
        Recorrer(Fila)
    elif Seleccion == 4:#Elimina a un cliente de la cola.
        #Llama a la función Eliminar y se almacena el resultado en la cola que vamos a modificar.
        Fila = Eliminar(Fila)
        
        #Muestra la cola modificada.
        print("\nLa cola actual es:")
        Recorrer(Fila)
    elif Seleccion == 5:#Ordenar la cola de clientes.
        #Llama a la función Ordenar y se almacena el resultado en la cola que vamos a modificar.
        Fila = Ordenar(Fila)

        #Muestra la cola ordenada alfabéticamente.
        print("\nLa cola se ordeno.")
        print("\nLa cola actual es:")
        Recorrer(Fila)
    elif Seleccion == 6:#Mezcla la cola.
        #Llama a la función Mezclar y se almacena el resultado en la cola que vamos a modificar.
        Fila = Mezclar(Fila)

        #Se muestra la cola mezclada.
        print("\nLa cola actual es:")
        Recorrer(Fila)
    elif Seleccion == 7:#Atiende a un cliente de la cola.
        #Llama a la función Atender y se almacena el resultado en la cola que vamos a modificar.
        Fila = Atender(Fila)

        #Se muestra la cola mezclada.
        print("\nLa cola actual es:")
        Recorrer(Fila)
    else:#Opción default.
        #Se muestra un mensaje de advertencia.
        print("\nLa opción que selecciono no existe.")
    
    return Fila  

# Función que agrega un cliente a la cola. 
def Insercion(Clientes):
    #El usuario ingresará el nombre del cliente.
    ClienteNuevo = input("Nombre del cliente nuevo: ")
   
    #Al ser una cola de clientes, se inserta el dato al final de la cola.
    Clientes.append(ClienteNuevo)
    
    #Retonamos la cola.
    return Clientes

#Función que busca en la cola a un cliente.
def Buscar(Clientes):
    #El usuario ingresará el nombre del cliente para buscar en la cola.
    ClienteABuscar = input("Ingrese el nombre del cliente que desea buscar: ")

    #Bucle que buscará al cliente en la cola.
    for ClienteActual in Clientes:
        #Si coincide, se le muestra al usuario un mensaje.
        if ClienteABuscar in ClienteActual:
            #Se imprime un mensaje.
            print(f'{ClienteABuscar} se encuentra en la cola.')
            return 
    
    #En caso de no coincidir, se le muestra un mensaje al usuario.
    print(f'{ClienteABuscar} no se encuentra en la cola.')

#Función que recorre la cola de clientes.
def Recorrer(Clientes):
    #Bucle que recorrera la cola.
    for ClienteActual in Clientes:
        #Se muestra la cola en pantalla.
        print(f'{ClienteActual}')

#Función que elimina a un cliente de la cola.
def Eliminar(Clientes):
    #Creamos una nueva cola con los valores de la cola actual para poder modificarla. 
    ColaNueva = Clientes

    #Se elimina por el nombre del cliente.
    try: 
        #Se ingresa el nombre del cliente, se elimina y se regresa la cola modificada.
        ClienteEliminar = input("Ingrese el nombre del cliente que desea eliminar: ")
        ColaNueva.remove(ClienteEliminar) 
        return ColaNueva
    #Excepción en caso de que el usuario ingresé un cliente que no este en la cola.
    except ValueError:
        print(f'\n{ClienteEliminar} no se encuentra en la cola.')
        return ColaNueva

#Función que ordena la cola de clientes.
def Ordenar(Clientes):
    #Obtenemos el tamaño de la cola.
    Tamaño= len(Clientes)

    for i in range(Tamaño):

        for j in range(0, Tamaño-i-1):

            if Clientes[j] > Clientes[j+1]:

                Clientes[j], Clientes[j+1] = Clientes[j+1], Clientes[j]

    return Clientes

#Función que mezcla la cola de clientes.
def Mezclar(Clientes):
    #Se mezcla la cola.
    random.shuffle(Clientes)

    #Se retorna la cola mezclada.
    return Clientes

#Función que atiende a un cliente en la cola.
def Atender(Clientes):
    #Se atiende al cliente más adelante en la cola.
    Clientes.popleft()

    #Se retorna la cola nueva.
    return Clientes

#Variable que le permitirá al usuario decidir salir o quedarse en el programa.
Salida = 2
 
#Inicia el programa y se modifica la lista de alumnos al realizar alguna operación.
Cliente = Entrada(Clientes)

#Bucle que permite permanecer en el programa y realizar varias operaciones.
while Salida != 1:
    #Mensaje para mostrar opciones de salida.
    print("\n¿Desea salir del programa?")
    print("1. Si.")
    print("2. No.")

    #Selección del usuario.
    Salida = int(input("Seleccione con el número: "))

    #El programa selecciona la ruta dependiendo de la selección del usuario.
    if Salida == 1:#Salir del programa.
        #Mensaje de despedida.
        print("Gracias por usar mi programa.")
    elif Salida ==2: #Quedarse en el programa.
        #Limpia la pantalla.
        os.system("cls")

        #Vuelve a mostrar las opciones y, al finalizar la operación, regresa la cola modificada. 
        Clientes = Opciones(Clientes)
    else: #Default.
        #Muestra un mensaje del error.
        print("Esa no es una opción.\n")