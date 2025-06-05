#Ejemplo de pilas estáticas en un historial de música.
#Importamos random para poder mezclar la pila.
import random

#Importamos os para poder limpiar la pantalla y tener un resultado más limpio.
import os

#Declaramos una pila de alumnos como ejemplo.
Historial = ['Lover', 'Viernes', 'Balaclava', 'Kumbala', 'Arabella', 'Querida', 'Mientes', 'Pose']
print("hola")

#Función que muestra la entrada al programa.
def Entrada(Historial):
    #Limpiamos la pantalla.
    os.system("cls")

    #Mostramos una pequeña presentación del programa.
    print("-----------------------------------------------------")
    print("             Bienvenido a tu historial               ")
    print("-----------------------------------------------------")

    #Mostramos las opciones.
    Historial = Opciones(Historial) 

    #Retornamos una pila con las modificaciones.
    return Historial

#Funcion que muestra las opciones del programa.
def Opciones(Historial):
    #Mostramos las opciones.
    print("    Opciones para escoger:")
    print("1. Escuchar una canción.")
    print("2. Buscar una canción en el historial.")
    print("3. Mostrar historial.")
    print("4. Eliminar canción del historial.")
    print("5. Ordenar historial alfabéticamente.")
    print("6. Mezclar historial.")

    #El usuario igresá su opción y en caso de ser inválido se muestra un mensaje.
    try:
        #Se selecciona una opción y se almacena en una variable para escoger la función a usar.
        Seleccion = int(input("Seleccione la opción que necesita con el número: "))
    except ValueError:
        #Excepción en caso de que el usuario ingresé un valor inválido.
        print("Esa no es una opción aceptable.") 

    #Creamos una nueva pila con los valores de la pila actual para poder modificarla.
    Pila = Historial

    #El programa selecciona la ruta dependiendo de la selección del usuario.
    if Seleccion == 1: #Inserta una canción en la pila.
        #Llama a la función Insertar y se almacena el resultado en la pila a modificar.
        Pila = Insertar(Pila)

        #Mostramos la pila en pantalla.
        print("\nEl historial actual es: ")
        Pila = Recorrer(Pila)

    elif Seleccion == 2:#Buscar una canción en la pila.
        #Llama a la función Buscar.
        Buscar(Pila)

    elif Seleccion == 3:#Recorre la pila de canciones y la muestra en pantalla.
        #Llama a la función Recorrer.
        Pila = Recorrer(Pila) 

    elif Seleccion == 4:#Elimina a una canción de la pila.
        #Llama a la función Eliminar y se almacena el resultado en la pila que vamos a modificar.
        Pila = Eliminar(Pila)
        
        #Muestra la pila modificada.
        print("\nEl historial actual es: ")
        Pila = Recorrer(Pila)
        
    elif Seleccion == 5:#Ordenar la pila de canciones.
        #Llama a la función Ordenar y se almacena el resultado en la pila que vamos a modificar.
        Pila = Ordenar(Pila)
        
    elif Seleccion == 6:#Mezcla la pila de canciones.
        #Llama a la función Mezclar y se almacena el resultado en la pila que vamos a modificar.
        Pila = Mezclar(Pila)   

        #Muestra la pila modificada.
        print("\nEl historial actual es: ")
        Pila = Recorrer(Pila)     

    else:#Opción default.
        #Se muestra un mensaje de advertencia.
        print("\nLa opción que selecciono no existe.")
    
    #Retorna la pila modificada.
    return Pila 

# Función que agrega una canción a la pila.
def Insertar(Historial):
    #El usuario ingresará el nombre del alumno.
    CancionNueva = input("Nombre de la canción que desea agregar: ")
   
    #Al ser una lista de alumnos, se inserta el dato al final de la lista.
    Historial.append(CancionNueva)
   
    #Retorna la pila modificada.
    return Historial

#Función que busca en la pila una canción.
def Buscar(Historial):
    #El usuario ingresará el nombre de la canción que buscará en el historial.
    CancionABuscar = input("Ingrese al usuario que desea buscar: ")

    #Bucle que buscará a la canción en el historial.
    for CancionActual in Historial:
        #Si coincide, se le muestra al usuario un mensaje.
        if CancionABuscar in CancionActual:
            #Se imprime un mensaje.
            print(f'Usted ha escuchado {CancionABuscar}.')
            return 
    
    #En caso de no coincidir, se le muestra un mensaje al usuario.
    print(f'Usted ha escuchado {CancionABuscar}.')

#Función que recorre el historial de canciones.
def Recorrer(Historial):
    #Creación de pila auxiliar que ayudará a mantener los datos.
    PilaAuxiliar = []

    #Bucle que recorrerá la pila.
    while Historial:
        #Se almacena la última canción en una variable.
        Cancion = Historial.pop()
        
        #Se agrega la canción a la pila auxiliar.
        PilaAuxiliar.append(Cancion)

        #Se muestra la última canción de la pila.
        print(Cancion)

    #Regresamos los datos del historial a la pila original.
    Historial = PilaAuxiliar[::-1]

    #Retornamos la pila.
    return Historial

#Función que elimina a una canción del historial.
def Eliminar(Historial):
    #Se ingresa el nombre de la canción que se desea eliminar.
    EliminarCancion = input("Escribe el elemento que desea eliminar: ")
    
    #Pila Auxiliar que nos ayudará a conservar los elementos.
    PilaAuxiliar = []
    
    #Bucle que recorre el historial.
    for i in range(len(Historial)-1, -1, -1):
        #En caso de no coincidir se le agrega el elemento a la pila auxiliar.
        if Historial[i] != EliminarCancion:
            PilaAuxiliar.append(Historial[i])
    
    #Se devuelven los valores a la pila original con el elemento eliminado.
    Historial = PilaAuxiliar[::-1]
    
    #Se retorna la pila.
    return Historial

#Función que ordena la pila de canciones.
def Ordenar(Historial):
    #Se ordena la pila alfabéticamente.
    Historial.sort()

    #Muestra la pila ordenada alfabéticamente.
    print("\n-----------------------------------------------------")
    print("              El historial se ordeno.                ")
    print("-----------------------------------------------------")
    print("\nEl historial actual es:")
    
    #Bucle que ayuda a mostrar la pila ordenada
    for Cancion in Historial:
        print(Cancion)

    #Se retorna la pila ordenada.
    return Historial

#Función que mezcla la pila de canciones.
def Mezclar(Historial):
    #Se mezcla la pila.
    random.shuffle(Historial)
    
    #Retornamos la pila mezclada.
    return Historial

#Variable que le permitirá al usuario decidir salir o quedarse en el programa.
Salida = 2

#Inicia el programa y se modifica la pila de canciones al realizar alguna operación.
Historial = Entrada(Historial)

#Bucle que permite permanecer en el programa y realizar varias operaciones.
while Salida != 1:
    #Mensaje para mostrar opciones de salida.
    print("\n¿Desea salir del programa?")
    print("1. Si.")
    print("2. No.")

    #Selección del usuario.
    Salida = int(input("Seleccione con el número: "))

    #El program selecciona la ruta dependiendo de la selección del usuario.
    if Salida == 1:#Salir del programa.
        #Limpia la pantalla.
        os.system("cls")
        #Mensaje de despedida.
        print("-----------------------------------------------------")
        print("          Gracias por visitar su historial.          ")
        print("-----------------------------------------------------")
    elif Salida ==2: #Quedarse en el programa.
        #Limpia la pantalla.
        os.system("cls")

        #Vuelve a mostrar las opciones y, al finalizar la operación, regresa la lista modificada. 
        Historial = Opciones(Historial)
    else: #Default.
        #Muestra un mensaje del error.
        print("Esa no es una opción.\n")