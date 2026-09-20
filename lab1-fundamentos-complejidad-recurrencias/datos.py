"""Funciones para generar los datos de prueba de los escenarios de Tamiza."""

import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla para generar siempre los mismos datos.

    Returns:
        Lista de n indices de riesgo distintos y desordenados.
    """
    datos = list(range(n))

    random.seed(semilla)
    random.shuffle(datos)

    return datos


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado para el escenario B.

    Args:
        n: cantidad de registros del lote.
        semilla: semilla para generar siempre los mismos datos.

    Returns:
        Lista con el 98% de los datos ordenados y el 2% restante
        desordenado al final.
    """
    random.seed(semilla)

    cantidad_nuevos = max(1, round(n * 0.02))

    nuevos = random.sample(range(n), cantidad_nuevos)
    nuevos_set = set(nuevos)

    ordenados = []

    for valor in range(n - 1, -1, -1):
        if valor not in nuevos_set:
            ordenados.append(valor)

    random.shuffle(nuevos)

    return ordenados + nuevos


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden contrario al requerido (escenario C).

    Args:
        n: cantidad de registros del lote.

    Returns:
        Lista de n indices de riesgo en orden ascendente.
    """
    return list(range(n))