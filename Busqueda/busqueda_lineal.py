def busqueda_secuencial(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

if __name__ == "__main__":
    datos = [3,4,6,7,8,10,9]
    elemento = 9

    indice = busqueda_secuencial(datos, elemento)
    if indice != -1:
        print(f"Elemento{elemento} encontrado en el índice: {indice}")
    else:
        print("Elemento {elemento} no encontrado en la lista.")
