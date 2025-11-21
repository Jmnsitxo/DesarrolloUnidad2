import random

# Generar 10 alertas con puntuaciones de riesgo entre 0 y 1
alertas = [random.random() for _ in range(10)]

print("Alertas generadas (riesgos originales):")
for i, riesgo in enumerate(alertas, start=1):
    print(f"Alerta {i}: {riesgo:.4f}")

# Implementar ordenamiento por selección (de mayor a menor)
for i in range(len(alertas) - 1):
    # Suponemos que el elemento actual es el mayor
    indice_max = i
    for j in range(i + 1, len(alertas)):
        if alertas[j] > alertas[indice_max]:
            indice_max = j
    # Intercambiar si encontramos uno mayor
    alertas[i], alertas[indice_max] = alertas[indice_max], alertas[i]

print("\nAlertas ordenadas por nivel de riesgo (de mayor a menor):")
for i, riesgo in enumerate(alertas, start=1):
    print(f"Prioridad {i}: {riesgo:.4f}")

# Ejemplo de interpretación:
print("\nInterpretación:")
print("Las alertas con puntuaciones más altas deben ser atendidas primero,")
print("ya que representan un mayor riesgo de fraude potencial.")
