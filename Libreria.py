#Programa que se encargará de administrar los libros de una librería, tanto organizarlos los libros como a los clientes.
#En todas las estructuras de datos se generará una estructura de ejemplo para agilizar el proceso.
#Importamos la librería random para aleatorizar métodos.
import random

#Importamos os para poder limpiar la pantalla y tener un resultado más limpio.
import os

#Importamos la extensión bisect para lograr la búsqueda binaria.
import bisect

#Importamos random para pode mezclar la cola.
from collections import deque

#Cola de clientes.
Clientes = deque(["Juan", "Cecilia", "Alfredo", "Josué", "José", "Carlos", "Ulises", "Mario", "Pedro"])

#Lista de clientes atendidos.
ListaClientesAtendidos = ["Katalina", "Tadeo"]

#Lista ID de libros estantería.
IDLibros = [15, 253, 98, 457, 33, 99, 157]

#Lista ID de libros estantería.
IDLibrosRecepcion = [12, 342, 545, 657, 23, 66, 85]

#Libros de la librería.
Libros = ["Ready player 2", "Don Quijote de la Mancha", "Cuarenta y siete leyes", "Entrevista con el vampiro", "La vuelta al mundo en ochenta días", "Viaje al centro de la Tierra", "La conjura de los necios"]

#Pila de libros en la recepción.
LibrosRecepcion = ["El diario de Ana Frank", "Rebelión en la granja", "Un mundo feliz", "Spanish beauty", "Vivir con nuestros muertos", "Todas nuestras maldiciones se cumplieron", "El gato que buscaba un nombre"]

#Función que muestra la entrada al programa.
def Entrada(Clientes, LibrosRecepcion, Libros, ListaClientesAtendidos, IDLibros, IDLibrosRecepcion):
    #Limpiamos la pantalla.
    os.system("cls")

    #Mostramos una pequeña presentación del programa.
    print("----------------------------------------------------------------------")
    print("                 Bienvenido a librería los árboles                    ")
    print("----------------------------------------------------------------------")

    #Mostramos las opciones.
    Recepcion(Clientes, LibrosRecepcion, Libros, ListaClientesAtendidos, IDLibros, IDLibrosRecepcion)

    #Cerramos el programa.
    return 

#Función que muestra la recepción.
def Recepcion(Clientes, LibrosRecepcion, Libros, ListaClientesAtendidos, IDLibros, IDLibrosRecepcion):
    #Variable utilizada para elegir una opción en la recepción.
    Eleccion = 1
    
    #Bucle utilicado para mantenerse en la recepción.
    while Eleccion != 0:
        #Mostramos una pequeña presentación del programa.
        print("-----------------------------Opciones---------------------------------")
        print("1. Clientes.")
        print("2. Pila de libros.")
        print("3. Libros del inventario.")
        print("0. Salir")

        #El usuario elige una opción.
        Eleccion = int(input("Seleccione con el número: "))

        #Opciones de la recepción.
        if Eleccion == 1:#Área de clientes.
            #LLama a la función del menú de clientes y las estructuras que se van a usar o modificar.
            Clientes, LibrosRecepcion, Libros, ListaClientesAtendidos, IDLibros, IDLibrosRecepcion = MostrarClientes(Clientes,  LibrosRecepcion, Libros, ListaClientesAtendidos, IDLibros, IDLibrosRecepcion)
        elif Eleccion == 2:#Pila de libros
            #LLama a la función del menú de la pila de libros y las estructuras que se van a usar o modificar.
            LibrosRecepcion, IDLibrosRecepcion = MostrarPilaLibros(LibrosRecepcion, IDLibrosRecepcion)
        elif Eleccion == 3:#
            #LLama a la función del menú de clientes y las estructuras que se van a usar o modificar.
            MostrarLibros(Libros, IDLibros)
    
    #Regresamos a la bienvenida.
    return 

#region Clientes
#Función que muestra el menú de clientes.
def MostrarClientes(Clientes, LibrosRecepcion, Libros, ListaClientesAtendidos, IDLibros, IDLibrosRecepcion):
    #Variable utilizada para elegir una opción en el menú.
    Eleccion = 1

    #Bucel utilizado para permanecer en el menú de clientes hasta que el usuario lo decida.
    while Eleccion != 0:
        #Limpiamos la pantalla.
        os.system("cls")

        #Presentación para la cola de clientes.
        print("------------------------------Cola de clientes-------------------------------")
    
        #Imprimimos la cola de clientes.
        RecorrerClientes(Clientes)

        #Mostramos el menú de opciones.
        print("------------------------Opciones de los clientes-----------------------------")
        print("1. Atender a cliente.")
        print("2. Buscar a cliente.")
        print("3. Eliminar a cliente por nombre.")
        print("4. Ordenar colas de clientes.")
        print("0. Regresar.")
    
        #El usuario elige la actividad a hacer econ el número.
        Eleccion = int(input("Seleccione con el número: "))

        #Opciones del menú.
        if Eleccion == 1:#Se atiende al cliente hasta adelante.
            #LLama a la función que atenderá un cliente y las estructuras que se van a usar o modificar.
            Clientes, LibrosRecepcion, Libros, ListaClientesAtendidos, IDLibros, IDLibrosRecepcion = AtenderACliente(Clientes, LibrosRecepcion, Libros, ListaClientesAtendidos, IDLibros, IDLibrosRecepcion)
        elif Eleccion == 2:#Busca a un cliente en la cola.
            #El usuario ingresará el nombre del cliente para buscar en la cola.
            ClienteABuscar = input("Ingrese el nombre del cliente que desea buscar: ")

            #Se busca al cliente y, en caso de encontrarlo, se regresa el lugar en la cola.
            LugarCliente = BuscarClienteCola(Clientes, ClienteABuscar)

            #En el caso de que se regrese un número distinto de -1 significa que se encontró al cliente y se muestra un mensaje-
            if LugarCliente != -1:
                #Se muestra el mensaje de que se encontró al cliente y en el lugar en el que se encuentra.
                print(f"{ClienteABuscar} se encuentra en la cola, en el lugar {LugarCliente}.")
            else :
                #Se manda un mensaje de que no se encontró el cliente.
                print(f"{ClienteABuscar} no se encuentra en la cola.")
            #Pequeña pausa para que el usuario aprecie el mensaje.
            input()
        elif Eleccion == 3:#Elimina a un cliente por el nombre.
            #LLama a la función EliminarClienteCola y las estructuras que se van a usar o modificar.
            Clientes = EliminarClienteCola(Clientes)
        elif Eleccion == 4:#Ordena la cola de clientes alfabéticamente.
            #LLama a la función de OrdenarClientes y las estructuras que se van a usar o modificar.
            Clientes = OrdenarClientes(Clientes)
        elif Eleccion == 0:#Sale del menú de clientes.
            #Rompe el bucle.
            break
        else:#Selección inválida.
            print("Seleccion inválida.")
    
    #Limpiamos la pantalla.
    os.system("cls")
    #Retorna las estructuras modificadas.
    return Clientes, LibrosRecepcion, Libros, ListaClientesAtendidos, IDLibros, IDLibrosRecepcion
    
#Se atiende a un cliente.
def AtenderACliente(Clientes, LibrosRecepcion, Libros, ListaClientesAtendidos, IDLibros, IDLibrosRecepcion):
    #Se intenta hacer el proceso.
    try :
        #Se atiende al cliente más adelante en la cola.
        ClienteAtendido = Clientes.popleft()
        
        #Se agrega el cliente atendido a una lista
        ListaClientesAtendidos.append(ClienteAtendido)

        #Se genera un número aleatorio para elegir de dónde el usuario tomará el libro que comprará.
        Numero = random.randint(1, 4)

        #Si el número es igual a 1 el usuario tomará un libro de la pila de la recepción, de otra manera, lo tomará de un de las estanterías.
        if Numero ==1:
            #Se intenta hacer el proceso.
            try:
                #LLama a la función EliminarLibroPila y las estructuras que se van a usar o modificar.
                LibrosRecepcion, IDLibrosRecepcion = EliminarLibroPila(LibrosRecepcion, IDLibrosRecepcion)
            #Excpeción en caso de no poder cumplir el proceso de eliminar un libro de una pila.
            except:
                #Se intenta hacer el proceso.
                try:
                    #LLama a la función EliminarLibroListas y las estructuras que se van a usar o modificar.
                    Libros, IDLibros = EliminarLibroLista(Libros, IDLibros)
                #Excepción en caso de que no se pueda eliminar el libro de las listas.
                except:
                    #Imprime un mensaje.
                    print("No hay libros disponibles.")
                    #Retorna las estructuras modificadas
                    return Clientes, LibrosRecepcion, Libros, ListaClientesAtendidos, IDLibros, IDLibrosRecepcion
        else:
            #Se intenta hacer le proceso.
            try:
                #LLama a la función EliminarLibroLista y las estructuras que se van a usar o modificar.#
                Libros, IDLibros = EliminarLibroLista(Libros, IDLibros)
            #Excepción en caso de que no se pueda eliminar el libro de las listas.  
            except:
                #Se imprime un mensaje.
                print("El cliente no encontró el libro que buscaba.")
                #Retorna las estructuras modificadas
                return Clientes, LibrosRecepcion, Libros, ListaClientesAtendidos, IDLibros, IDLibrosRecepcion
        #Se retorna la cola nueva.
        return Clientes, LibrosRecepcion, Libros, ListaClientesAtendidos, IDLibros, IDLibrosRecepcion
    #Excepción en caso de no tener libros en la librería.
    except:
        #Imprime un mensaje.
        print("No hay clientes que atender.")
        #Retorna las estructuras modificadas
        return Clientes, LibrosRecepcion, Libros, ListaClientesAtendidos, IDLibros, IDLibrosRecepcion

#Búsqueda lineal.
#Función que  usa la búsqueda lineal para buscar en la cola a un cliente.
def BuscarClienteCola(Clientes, ClienteABuscar):
    #Bucle que buscará al cliente en la cola.
    for i in range(len(Clientes)):
        #Si coincide, se le muestra al usuario un mensaje.
        if Clientes[i] == ClienteABuscar:
            #Retorna el lugar del cliente.
            return  i + 1
    #Retorna -1 en caso de no encontrar al cliente.
    return -1

#Función que elimina a un cliente de la cola.
def EliminarClienteCola(Clientes):
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
        #Imprime un mensaje.
        print(f'\n{ClienteEliminar} no se encuentra en la cola.')
        #Retornamos la cola modificada.
        return ColaNueva

#Función que recorre la cola y la imprime en pantalla.
def RecorrerClientes(Clientes):
    #Intentamos recorrer la cola.
    try:
        #Bucle que recorrerá la cola.
        for ClienteActual in Clientes:
            #Se muestra la cola en pantalla.
            print(f'{ClienteActual}')
    #Excepción en caso de que la cola este vacía.
    except:
        #Imprimimos el mensaje de la excepción.
        print("La cola de clientes está vacía.")
        #Damos una pausa para que le usuario aprecie el mensaje.
        input("Presione una tecla para regresar.")

#Método burbuja.
#Función que se encarga de ordenar la cola de clientes con el método burbuja.
def OrdenarClientes(Clientes):
    #Intentamos ordenar la cola.
    try:
        #Tomamos la longitud de la cola y la agregamos a una variable.
        Longitud = len(Clientes)

        #Bucle que recorrera la cola.
        for i in range(Longitud):
            #Bucel que repetira las acciones hasta que la cola esté ordenada.
            for j in range(0, Longitud-i-1):
                #En caso de que el primero sea mayor al siguiente, intercambia sus valores.
                if Clientes[j] > Clientes[j+1]:
                    Clientes[j], Clientes[j+1] = Clientes[j+1], Clientes[j]
    #Excepción en caso de que la cola se encuentre vacía.
    except:
        #Imprimimos un mensaje.
        print("La cola de clientes está vacía.")
        #Pausa para que el usuario pueda apreciar el mensaje.
        input("Presione una tecla para regresar.")
    #Retornamos la colaordenada.
    return Clientes
#endregion

#region Pila
#Función que muestra el menú de la pila de libros.
def MostrarPilaLibros(LibrosRecepcion, IDLibrosRecepcion):
    #Variable utilizada para elegir una opción en la recepción.
    Eleccion = 1

    #Bucle que nos ayuda a mantenernos en en menú de la pila de libros.
    while Eleccion != 0:
        #Limpiamos la pantalla.
        os.system("cls")

        #Presentación de la pila de libros
        print("------------------------------Pila de libros-------------------------------")
    
        #Imprimimos la pila de libros en la recepción.
        LibrosRecepcion = RecorrerPilaLibros(LibrosRecepcion)
        IDLibrosRecepcion = RecorrerPilaLibros(IDLibrosRecepcion)
        
        #Mostramos una pequeña presentación del programa.
        print("----------------Opciones de los libros en la recepción---------------------")
        print("1. Sacar un libro al azar.")
        print("2. Buscar libro.")
        print("3. Ordenar libros.")
        print("0. Regresar.")
    
        #El usuario ingresa su elección.
        Eleccion = int(input("Seleccione con el número: "))

        #Se elige el camino dependiendo lo que el usuario escogio.
        if Eleccion == 1:#Saca un libro al azar.
            #Llama a la función EliminarLibroPila y a las estructuras que se van a modificar.
            LibrosRecepcion = EliminarLibroPila(LibrosRecepcion)   
        elif Eleccion == 2:#Busca un libro en la pila.
            #El usuario ingresará el nombre del cliente para buscar en la cola.
            LibroABuscar = input("Ingrese el nombre del LIBRO que desea buscar: ")

            #Se llama a la función BuscarLibroPila y se le da el valor del lugar a una variable.
            LugarLibro =  BuscarLibroPila(LibrosRecepcion, LibroABuscar)

            #En caso de ser -1 el libro no se encontró, de otra forma se muestra un mensaje con el lugar del libro en la pila.
            if LugarLibro != -1:
                #Imprimimos un mensaje.
                print(f"{LibroABuscar} se encuentra en la pila, en el lugar {LugarLibro}.")
            else :
                #Imprimimos un mensaje de que el libro no se encontró.
                print(f"{LibroABuscar} no se encuentra en la pila.")
            #El programa hace una pausa para que el usuario aprecie el mensaje. 
            input()
        elif Eleccion == 3:#Ordena la pila de libros afabéticamente
            #Llama a la función OrdenarPila y a las estructuras que se van a modificar.
            LibrosRecepcion, IDLibrosRecepcion = OrdenarPila(LibrosRecepcion, IDLibrosRecepcion)
        elif Eleccion == 0:#Sale del menú de la pila de libros.
            #Rompe el bucle y vuelve a la recepción.
            break
        else:#Selección inválida.
            #Se muestra un mensaje.
            print("Seleccion inválida.")
    
    #Limpiamos la pantalla.
    os.system("cls")
    #Retornamos los valores de las estructuras modificadas.
    return LibrosRecepcion, IDLibrosRecepcion

#Función que elimina un libro de la pila de forma al azar.
def EliminarLibroPila(LibrosRecepcion, IDLibrosRecepcion):
    #Validación en caso de que la pila esté vacía.
    if len(LibrosRecepcion) == 0:
        #Imprimimos un mensaje y creacmos una pausa para que el usuario la vea.
        print("La pila de libros está vacía.")
        input()
        #Retornamos la pila sin modificar.
        return LibrosRecepcion
    
    # Generar un índice aleatorio
    NumeroAleatorio = random.randrange(len(LibrosRecepcion))

    # Eliminar el elemento aleatorio de la pila junto con su ID de la lista.
    LibrosRecepcion.pop(NumeroAleatorio)
    IDLibrosRecepcion. pop(NumeroAleatorio)

    #Retornamos las estructuras modificadas.
    return LibrosRecepcion, IDLibrosRecepcion

#Función que Recorre la pila de libros.
def RecorrerPilaLibros(LibrosRecepcion):
    #Creación de pila auxiliar que ayudará a mantener los datos.
    PilaAuxiliar = []

    #Validación en caso de que la pila se encuentre vacía.
    if len(LibrosRecepcion) == 0:
        #Imprimimos un mensaje y creamos una pausa para que el usuario lea el mensaje.
        print("La pila de libros está vacía.")
        input()
        #Retornamos la pila.
        return LibrosRecepcion
    
    #Bucle que recorrerá la pila.
    while LibrosRecepcion:
        #Se almacena la última canción en una variable.
        Libro = LibrosRecepcion.pop()
        
        #Se agrega la canción a la pila auxiliar.
        PilaAuxiliar.append(Libro)

        #Se muestra el último libro de la pila.
        print(Libro)

    #Regresamos los datos de la pila a la pila original.
    LibrosRecepcion = PilaAuxiliar[::-1]

    #Retornamos la pila.
    return LibrosRecepcion

#Búsqueda lineal.
#Función que busca un libro en la pila con la búsqueda lineal.
def BuscarLibroPila(LibrosRecepcion, LibroABuscar):
    #Validación en caso de que la pila se encuentre vacía.
    if len(LibrosRecepcion) == 0:
        #Imprimimos un mensaje y creamos una pausa para que el usuario lea el mensaje.
        print("La pila de libros está vacía.")
        input()
        #Retornamos -1 para indicar que no se encontró el libro.
        return -1
    
    #Bucle que buscará al libro en la pila.
    for i in range(len(LibrosRecepcion)):
        #Si coincide, se le muestra al usuario un mensaje.
        if LibrosRecepcion[i] == LibroABuscar:
            #Retornamos el lugar del libro en la pila.
            return  i
    #Retornamos -1 para indicar que no se encontró el libro.
    return -1

#Ordenamiento por selección y Ordenamiento por inserción.
#Función que ordena la pila por selección o por inserción.
def OrdenarPila(LibrosRecepcion, IDLibrosRecepcion):
    #Opciones para el usuario.
    print("------------------------Opciones de ordenamiento----------------------------")
    print("1. Ordenar por nombre.")
    print("2. Ordenar por ID.")

    #El usuario elige su opción con el número.
    Eleccion = int(input("Seleccione con el número: "))

    #Dependiendo de la elección del usuario se seguirá un camino de ordenamiento.
    if Eleccion == 1:#Por selección.
        #Validación en caso de que la pila estpe vacía.
        if len(LibrosRecepcion) == 0:
            #Imprimimos un mensaje y creamos un tiempo para que el usuario lea el mensaje.
            print("La pila de libros está vacía.")
            input()
            #Retornamos la pila.
            return LibrosRecepcion
        
        #Bucle con el que se recorre la pila.
        for i in range(len(LibrosRecepcion)):
            #Valor que se asume que es el mínimo en la pila.
            IndiceMinimo = i
            #Bucle que busca el elemento mínimo en la pila.
            for j in range(i+1, len(LibrosRecepcion)):
                #Si el valor es menor que en el indice mínimo intercambiamos los valores del índice mínimo.
                if LibrosRecepcion[j] < LibrosRecepcion[IndiceMinimo]:
                    IndiceMinimo = j
            #Cambiamos los valores del índice mínimo y el siguiente indice para ordenar los valores.
            LibrosRecepcion[i], LibrosRecepcion[IndiceMinimo],  IDLibrosRecepcion[i], IDLibrosRecepcion[IndiceMinimo] = LibrosRecepcion[IndiceMinimo], LibrosRecepcion[i], IDLibrosRecepcion[i], IDLibrosRecepcion[IndiceMinimo]
    elif Eleccion ==2:#Por incersión.
        #Itera por la pilaasumiendo que el primer elemnto ya está en su posición correcta.
        for i in range(1, len(IDLibrosRecepcion)):
            #El elemento actual se almacena en una variable.
            LlaveItem = IDLibrosRecepcion[i]
            NombreLibro = LibrosRecepcion[i]
            #Variable que rastrearáel elemento que se compare con la llave.
            j = i-1
            #Bucle con el cual se desplaza los valores mayores de la llave a la derecha.
            while j>= 0 and LlaveItem < IDLibrosRecepcion[j]:
                #Se desplazan los valores mayores a la derecha.
                IDLibrosRecepcion[j+1] = IDLibrosRecepcion[j]
                LibrosRecepcion[j+1] = LibrosRecepcion[j]
                #Decrementamos j.
                j-=1
            #Las llaves se insertan en el lugar índicado.
            IDLibrosRecepcion[j+1]= LlaveItem
            LibrosRecepcion[j+1] = NombreLibro

    #Retornamos las estructuras modificadas
    return LibrosRecepcion, IDLibrosRecepcion

#endregion

#region Lista
#Función que muestra el menú de los libros de las estanterías.
def MostrarLibros(Libros, IDLibros):
    #Variable utilizada para elegir una opción en la recepción.
    Eleccion = 1

    #Bucle que nos ayuda a mantenernos en en menú de la pila de libros.
    while Eleccion != 0:
        #Limpiamos la pantalla.
        os.system("cls")

        #Presentación para los libros de estantería,
        print("------------------------------Lista de libros--------------------------------")
    
        #Imprimimos los libros.
        RecorrerLibros(Libros)

        #Mostramos una pequeña presentación del programa.
        print("-------------------------Opciones de los libros------------------------------")
        print("1. Sacar un libro al azar.")
        print("2. Buscar libro.")
        print("3. Ordenar libros.")
        print("0. Regresar.")
    
        #El usuario elige la opción con el número.
        Eleccion = int(input("Seleccione con el número: "))

        #Opciones de ka estantería de libros.
        if Eleccion == 1:#Sacar un libro al azar.
            #LLama a la función EliminarLibroLista y las estructuras que se van a usar o modificar.
            Libros = EliminarLibroLista(Libros)
        elif Eleccion == 2:#Busca un libro en la lista.
            #El usuario ingresará el nombre del libropara buscar en la lista.
            LibroABuscar = input("Ingrese el nombre del cliente que desea buscar: ")

            #LLama a la función que buscar un libro en la lista y las estructuras que se van a usar o modificar.
            LugarLibro = BuscarLibroLista(Libros, LibroABuscar, IDLibros)

            #En caso de ser -1 el libro no se encontró, de otra forma se muestra un mensaje con el lugar del libro en la lista.
            if LugarLibro != -1:
                #Imprimimos un mensaje
                print(f"{LibroABuscar} se encuentra en la cola, en el lugar {LugarLibro}.")
            else :
                #Imprimimos un mensaje de que no se encontró el libro en la lista.
                print(f"{LibroABuscar} no se encuentra en la lista.")
            #Creamos una pausa para que el usuario vea el mensaje.
            input()
        elif Eleccion == 3:#Ordena la lista de libros alfabéticamente.
            #LLama a la función que prdenará la lista y sus IDs, y las estructuras que se van a usar o modificar.
            IDLibros = OrdenarLibrosLista(IDLibros)
            Libros = OrdenarLibrosLista(Libros)
        elif Eleccion == 0:#Sale del menú.
            #Rompe el ciclo.
            break
        else:#Opción inválida.
            #Mostramos un mensaje.
            print("Seleccion inválida.")
    #Limpiamos la pantalla.
    os.system("cls")
    #Retornamos las estructuras modificadas.
    return Libros, IDLibros

#Función que recorre la lista y la imprime en pantalla.
def RecorrerLibros(Libros):
    #Bucle que recorrera la lista.
    for LibroActual in Libros:
        #Se muestra la lista en pantalla.
        print(f'{LibroActual}')
    return

#Función que elimina un libro aleatorio de la lista.
def EliminarLibroLista(Libros, IDLibros):
    #Validación en caso de que la lita esté vacía.
    if len(Libros) == 0:
        #Imprimimos un mensaje y creamos un tiempo para que el usuario lo lea.
        print("La pila de libros está vacía.")
        input()
        #Retornamos las lista.
        return Libros
    
    #Generar un índice aleatorio
    NumeroAleatorio = random.randrange(len(Libros))

    #Eliminar el elemento aleatorio de la lista junto con su ID de la lista.
    Libros.pop(NumeroAleatorio)
    IDLibros.pop(NumeroAleatorio)

    #Retornamos las listas modificadas.
    return Libros, IDLibros

#Búsqueda binaria.
#Función que busca un libro en la lista.
def BuscarLibroLista(Libros, LibroABuscar, IDLibros):
    #Lugar en lista que incrementará a medida que se busca en la lista.
    LugarLista = 0

    #Bucle que buscará al libro en la lista.
    for LibroActual in Libros:
        #Si coincide, se le muestra al usuario un mensaje.
        if LibroABuscar in LibroActual:
            break
        #Incremento del número de lista
        LugarLista += 1

    #Mensaje para alertar al usuario.
    print("Para usar este método necesita ordenar la lista")

    #Llama a la función OrdenarLibrosLiesta y a las estructuras que se vana modificar.
    IDLibros = OrdenarLibrosLista(IDLibros)

    #Se almacena el ID en una variable para comparar y encontrar el libro en base a su ID.
    IdLibro = IDLibros[LugarLista]

    #Método Binario.
    #Se crea el máximo y mínimo de los valores en la lista
    Izquierda = 0
    Derecha = len(IDLibros) - 1

    #Bucle que sirve para recorrer y partir la lista para encontrar el libro.
    while Izquierda <= Derecha:
        #Sacamos la media de la lista.
        Mitad = (Izquierda + Derecha) // 2

        #En caso de ser igual retornamos el valor del elemento.
        if IDLibros[Mitad] == IdLibro:
            return Mitad 
        #Si es menor, se toma el valor derecho de la lista y se busca en ese espacio.
        elif IDLibros[Mitad] < IdLibro:
            Izquierda = Mitad + 1
        #De otra forma, se toma el valor izquierdo y se busca ahí.
        else:
            Derecha = Mitad - 1
    #Retornamos -1 en caso de no encontrar el elemmento.
    return -1

#Métodos recursivos
#Función que ordena los el ID de los libros.
def OrdenarLibrosLista(IDLibros): 
    #Método quicksort.
    #Si la longitud de la lista es 0 o 1 se retorna porque ya está ordenada.
    if len(IDLibros) <= 1:
        return IDLibros
    else:
        #Creamos un pivote.
        pivot = IDLibros[0]

        # Selecciona los elementos menores y mayores que el pivote
        menores = [x for x in IDLibros[1:] if x <= pivot]
        mayores = [x for x in IDLibros[1:] if x > pivot]
        
        #Retornamos la lista ya ordenada.
        return OrdenarLibrosLista(menores) + [pivot] + OrdenarLibrosLista(mayores)

#endregion

#Llamamos a la función para iniciar el programa.
Entrada(Clientes, LibrosRecepcion, Libros, ListaClientesAtendidos, IDLibros, IDLibrosRecepcion)