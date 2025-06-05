#Ejemplo de listas estáticas en una escuela con la lista de alumnos.
#Importamos random para pode mezclar la lista.
import random

#Importamos os para poder limpiar la pantalla y tener un resultado más limpio.
import os

#Declaramos una lista de alumnos como ejemplo.
Alumnos = ['Mauricio', 'Galilea', 'Ricardo', 'Juan', 'Katherine']

#Función que muestra la entrada al programa.
def Entrada(Alumnos):
    #Limpiamos la pantalla.
    os.system("cls")

    #Mostramos una pequeña presentación del programa.
    print("------------------------")
    print("Bienvenido al Listathon")
    print("------------------------")

    #Mostramos las opciones.
    Alumnos = Opciones(Alumnos) 

    #Retornamos una lista con las modificaciones.
    return Alumnos

#Funcion que muestra las opciones del programa.
def Opciones(Alumnos):
    #Mostramos las opciones
    print("    Opciones para escoger:")
    print("1. Insertar un alumno a la lista.")
    print("2. Buscar un alumno de la lista.")
    print("3. Mostrar la lista de alumnos.")
    print("4. Eliminar alumno de la lista.")
    print("5. Ordenar lista de alumnos.")
    print("6. Mezclar lista de alumnos.")

    #Se selecciona una opción y se almacena en una variable para escoger la función a usar.
    Seleccion = int(input("Seleccione la opción que necesita con el número: "))
    
    #Creamos una nueva lista con los valores de la lista actual para poder modificarla.
    Lista = Alumnos

    #El program selecciona la ruta dependiendo de la seleccioón del usuario.
    if Seleccion == 1: #Inserta un alumno en la lista.
        #Llama a la función inserción y se almacena el resultado en la lista que vamos a modificar.
        Lista = Insercion(Lista)

        #Mostramos la lista en pantalla.
        print("\nLa lista actual es: ")
        RecorrerListaAlumnos(Lista)

    elif Seleccion == 2:#Buscar un alumno en la lista.
        #Llama a la función BuscarAlumno.
        BuscarAlumno(Lista)

    elif Seleccion == 3:#Recorre la lista de alumnos y la muestra en pantalla.
        #Llama a la función RecorrerListaAlumnos.
        RecorrerListaAlumnos(Lista)

    elif Seleccion == 4:#Elimina a un alumno de la lista.
        #Llama a la función AlumnoEliminar y se almacena el resultado en la lista que vamos a modificar.
        Lista = EliminarAlumno(Lista)
        
        #Muestra la lista modificada.
        print("\nLa lista actual es:")
        RecorrerListaAlumnos(Lista)
    elif Seleccion == 5:#Ordenar la lista de alumnos.
        #Llama a la función Ordenar y se almacena el resultado en la lista que vamos a modificar.
        Lista = Ordenar(Lista)

        #Muestra la lista ordenada alfabéticamente.
        print("\nLa lista se ordeno.")
        print("\nLa lista actual es:")
        RecorrerListaAlumnos(Lista)
    elif Seleccion == 6:#Mezcla la lista.
        #Llama a la función MezcclarLista y se almacena el resultado en la lista que vamos a modificar.
        Lista = MezclarLista(Lista)

        #Se muestra la lista mezclada.
        print("\nLa lista actual es:")
        RecorrerListaAlumnos(Lista)
    else:#Opción default.
        #Se muestra un mensaje de advertencia.
        print("\nLa opción que selecciono no existe.")
    
    return Lista   

# Función que agrega alumnos a la lista 
def Insercion(Alumnos):
    #Se almacena la nueva longitud para insertar al nuevo alumno al final de la lista.
    AlumnosCantidadNueva = len(Alumnos) + 1 

    #El usuario ingresará el nombre del alumno.
    AlumnoNuevo = input("Nombre del usuario que desea agregar: ")
   
    #Al ser una lista de alumnos, se inserta el dato al final de la lista.
    Alumnos.insert(AlumnosCantidadNueva,AlumnoNuevo)
   
    return Alumnos

#Función que busca en la lista a un alumno.
def BuscarAlumno(Alumnos):
    #El usuario ingresará el nombre del alumno para buscar en la lista.
    AlumnoABuscar = input("Ingrese al usuario que desea buscar: ")

    #Número de lista que incrementará a medida que se busca en la lista.
    NumeroLista = 1

    #Bucle que buscará al alumno en la lista.
    for AlumnoActual in Alumnos:
        #Si coincide, se le muestra al usuario un mensaje.
        if AlumnoABuscar in AlumnoActual:
            print(f'{AlumnoABuscar} se encuentra en la lista y su número de lista es {NumeroLista}')
            return 

        #Incremento del número de lista
        NumeroLista += 1
    
    #En caso de no coincidir, se le muestra un mensaje al usuario.
    print(f'{AlumnoABuscar} no se encuentra en la lista')

#Función que recorre la lista de alumnos.
def RecorrerListaAlumnos(Alumnos):
    #Número de lista que incrementará a medida que se muestra la lista.
    NumeroLista = 1

    #Bucle que recorrera la lista.
    for AlumnoActual in Alumnos:
        #Se muestra la lista en pantalla.
        print(f'{NumeroLista}. {AlumnoActual}')

        #Incremento del número de lista.
        NumeroLista += 1 

#Función que elimina a alumnos de la lista.
def EliminarAlumno(Alumnos):
    #Creamos una nueva lista con los valores de la lista actual para poder modificarla. 
    ListaNueva = Alumnos

    #Se muestra las opciones para la eliminación.
    print("\n1. Eliminar por nombre")
    print("2. Eliminiar por número de lista")

    #El usuario elige la opción.
    OpcionEliminacion = int(input("\nElija la opción para eliminar al alumno: "))

    #Se muestra la lista para que le facilite al usuario encontrar al alumno.
    RecorrerListaAlumnos(ListaNueva)

    #Se elimina por el nombre del alumno.
    if OpcionEliminacion == 1:
        try: 
            #Se ingresa el nombre del alumno, se elimina y se regresa la lista modificada.
            AlumnoEliminar = input("Ingrese el nombre del alumno que desea eliminar: ")
            ListaNueva.remove(AlumnoEliminar) 
            return ListaNueva
        #Excepción en caso de que el usuario ingresé un alumno que no estre en la lista.
        except ValueError:
            print(f'\n{AlumnoEliminar} no se encuentra en la lista.')
            return ListaNueva

    #Caso por número de lista.
    elif OpcionEliminacion == 2:
        try:
            #Se ingresa el nombre del alumno.
            NumeroAlumnoEliminar = int(input("Ingrese el número de lista del alumno a eliminar: "))
            #Se elimina al alumno y se regresa la lista modificada.
            ListaNueva.pop(NumeroAlumnoEliminar-1)
            return ListaNueva
        except ValueError:#Excepción de valor no válido.
            print(f'\n{NumeroAlumnoEliminar} no se encuentra en la lista.')
            return ListaNueva
        except IndexError:#Excepción en caso de que el usuario ingrese un número de lista inexistente.
            print(f'\n{NumeroAlumnoEliminar} no se encuentra en la lista.')
            return ListaNueva
    
    #Usuario ingreso una opción no válida.
    print("Opción no válida.")

    #Se retorna la lista.
    return ListaNueva

#Función que ordena la lista de alumnos
def Ordenar(Alumnos):
    #Se ordena la lista.
    Alumnos.sort()

    #Se retorna la lista ordenada.
    return Alumnos

#Función que mezcla la lista de alumnos.
def MezclarLista(Alumnos):
    #Se mezcla la lista.
    random.shuffle(Alumnos)

    #Se retornala lista mezclada.
    return Alumnos

#Variable que le permitirá al usuario decidir salir o quedarse en el programa.
Salida = 2

#Inicia el programa y se modifica la lista de alumnos al realizar alguna operación.
Alumnos = Entrada(Alumnos)

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
        #Mensaje de despedida.
        print("Gracias por usar Listathon.")
    elif Salida ==2: #Quedarse en el programa.
        #Limpia la pantalla.
        os.system("cls")

        #Vuelve a mostrar las opciones y, al finalizar la operación, regresa la lista modificada. 
        Alumnos = Opciones(Alumnos)
    else: #Default.
        #Muestra un mensaje del error.
        print("Esa no es una opción.\n")