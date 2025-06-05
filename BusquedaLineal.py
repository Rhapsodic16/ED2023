def BusquedaLineal(array, x):
    for i in range(len(array)):
        if array[i]== x:
            return i
    return -1

array = [1, 3, 5, 65, 78, 90]

x = 78

Resultado = BusquedaLineal(array,x)

if Resultado != -1:
    print(f"El número {x} se encuentra en el índice {Resultado} del arreglo.")
else :
    print(f"El número {x} no se encuentra en el arreglo.")