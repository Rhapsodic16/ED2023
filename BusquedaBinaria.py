def BusquedaBinaria(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 70]
x = 3

Resultado = BusquedaBinaria(array,  x)

if Resultado != -1:
    print("Elemento encontrado en la posición: ", str(Resultado))
