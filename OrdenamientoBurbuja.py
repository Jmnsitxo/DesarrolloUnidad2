def burbuja(Lista):
    n = len(Lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if Lista[j] > Lista[j+1]:
                Lista[j], Lista[j+1] = Lista[j+1], Lista[j]
    return Lista

numeros = [5, 2, 9, 1, 5, 6]
print("Lista original:", numeros)
numeros_ordenados = burbuja(numeros)
print("Lista ordenada:", numeros_ordenados)