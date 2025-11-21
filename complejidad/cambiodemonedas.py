monedas = [500, 200, 100, 50, 25, 5, 1]

def devolver_cambio(cantidad: int, monedas: list) -> list:
    """Devuelve una lista de monedas que suman (hasta) la cantidad usando el
    algoritmo voraz. Asume que `monedas` está ordenada de mayor a menor y que
    `cantidad` y las monedas son enteros (por ejemplo, centavos).

    Retorna la lista de monedas usadas (puede estar vacía si `cantidad` es 0).
    """
    cambio = []
    for moneda in monedas:
        if cantidad <= 0:
            break
        # usar división entera en lugar de bucle while (más eficiente)
        cuenta = cantidad // moneda
        if cuenta:
            cambio.extend([moneda] * cuenta)
            cantidad = cantidad % moneda
    return cambio


if __name__ == "__main__":
    # cantidad inicial (ejemplo)
    cantidad_inicial = 786
    cambio = devolver_cambio(cantidad_inicial, monedas)
    # comprobar que el cambio suma correctamente
    suma_cambio = sum(cambio)
    cantidad_restante = cantidad_inicial - suma_cambio

    print("Cantidad inicial:", cantidad_inicial)
    print("Cambio:", cambio)
    from collections import Counter
    resumen = Counter(cambio)
    print("Resumen:")
    for m in monedas:
        if resumen.get(m, 0):
            print(f"  {m}: {resumen[m]}")
    print("Suma de cambio:", suma_cambio)
    print("Cantidad restante:", cantidad_restante)