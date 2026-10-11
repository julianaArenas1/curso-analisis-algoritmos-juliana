"""Pruebas para los algoritmos de subarreglo maximo."""

import random

from subarreglo import (
    subarreglo_fuerza_bruta,
    subarreglo_maximo,
)


def probar_suma(valores: list[float], suma_esperada: float) -> None:
    fuerza_bruta = subarreglo_fuerza_bruta(valores)
    divide_venceras = subarreglo_maximo(
        valores,
        0,
        len(valores) - 1,
    )

    assert fuerza_bruta[2] == suma_esperada
    assert divide_venceras[2] == suma_esperada


# Serie del problema
probar_suma(
    [-3, 5, -2, 8, -6, 3, 9, -4],
    17,
)

# Un solo elemento
probar_suma(
    [7],
    7,
)

# Todos negativos
probar_suma(
    [-5, -2, -8, -1],
    -1,
)

# Todos positivos
probar_suma(
    [2, 4, 1, 3],
    10,
)

# El mejor tramo cruza el punto medio
probar_suma(
    [-2, 5, -1, 4, -3],
    8,
)

# Comparacion con listas aleatorias
random.seed(42)

for _ in range(20):
    cantidad = random.randint(1, 20)

    valores = [
        random.randint(-20, 20)
        for _ in range(cantidad)
    ]

    fuerza_bruta = subarreglo_fuerza_bruta(valores)
    divide_venceras = subarreglo_maximo(
        valores,
        0,
        len(valores) - 1,
    )

    assert fuerza_bruta[2] == divide_venceras[2]

print("Todas las pruebas pasaron correctamente.")
