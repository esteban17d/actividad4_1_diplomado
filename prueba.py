def calcular_promedio(notas):
    """Calcula el promedio de una lista de notas.

    Args:
        notas: Una lista de notas numéricas.

    Returns:
        El promedio de las notas.
    """
    return sum(notas) / len(notas)

def calcular_mediana(notas):
    """Calcula la mediana de una lista de notas.

    Args:
        notas: Una lista de notas numéricas ordenadas.

    Returns:
        La mediana de las notas.
    """
    n = len(notas)
    if n % 2 == 0:
        return (notas[n//2-1] + notas[n//2]) / 2
    else:
        return notas[n//2]

def validar_notas(notas):
    """Valida que todas las notas estén dentro de un rango válido (0-100).

    Args:
        notas: Una lista de notas.

    Returns:
        True si todas las notas son válidas, False en caso contrario.
    """
    for nota in notas:
        if nota < 0 or nota > 100:
            return False
    return True

if __name__ == "__main__":
    notas = []
    for i in range(4):
        while True:
            try:
                nota = int(input(f"Ingresa la nota {i+1}: "))
                if 0 <= nota <= 100:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 100.")
            except ValueError:
                print("Ingresa un valor numérico.")

    if validar_notas(notas):
        notas.sort()
        promedio = calcular_promedio(notas)
        mediana = calcular_mediana(notas)
        nota_maxima = max(notas)
        nota_minima = min(notas)

        print(f"Promedio: {promedio:.2f}")
        print(f"Mediana: {mediana}")
        print(f"Nota más alta: {nota_maxima}")
        print(f"Nota más baja: {nota_minima}")

        print("\nInforme de notas:")
        for i, nota in enumerate(notas):
            print(f"Nota {i+1}: {nota}")
    else:
        print("Al menos una de las notas ingresadas es inválida.")
