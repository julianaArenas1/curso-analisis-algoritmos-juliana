"""Medicion de tiempos de los algoritmos de subarreglo maximo."""

import random
import time

from matplotlib import pyplot as plt

from subarreglo import (
    subarreglo_fuerza_bruta,
    subarreglo_maximo,
)

plt.switch_backend("Agg")


TAMANOS = [10, 50, 100, 500, 1000, 2000, 4000]
REPETICIONES = 3
SEMILLA = 42


def medir_fuerza_bruta(valores: list[float]) -> tuple[float, float]:
    """Mide el tiempo promedio del algoritmo de fuerza bruta.

    Args:
        valores: lista de valores que se va a analizar.

    Returns:
        Una tupla con el tiempo promedio y la suma maxima encontrada.
    """
    tiempos = []
    suma_maxima = 0.0

    for _ in range(REPETICIONES):
        inicio = time.perf_counter()

        resultado = subarreglo_fuerza_bruta(valores)

        fin = time.perf_counter()

        tiempos.append(fin - inicio)
        suma_maxima = resultado[2]

    promedio = sum(tiempos) / len(tiempos)

    return promedio, suma_maxima


def medir_divide_venceras(valores: list[float]) -> tuple[float, float]:
    """Mide el tiempo promedio del algoritmo divide y venceras.

    Args:
        valores: lista de valores que se va a analizar.

    Returns:
        Una tupla con el tiempo promedio y la suma maxima encontrada.
    """
    tiempos = []
    suma_maxima = 0.0

    for _ in range(REPETICIONES):
        inicio = time.perf_counter()

        resultado = subarreglo_maximo(
            valores,
            0,
            len(valores) - 1,
        )

        fin = time.perf_counter()

        tiempos.append(fin - inicio)
        suma_maxima = resultado[2]

    promedio = sum(tiempos) / len(tiempos)

    return promedio, suma_maxima


def main() -> None:
    """Ejecuta las mediciones y genera la grafica comparativa."""
    generador = random.Random(SEMILLA)

    tiempos_fuerza_bruta = []
    tiempos_divide_venceras = []

    for n in TAMANOS:
        valores = [
            generador.randint(-100, 100)
            for _ in range(n)
        ]

        tiempo_bruta, suma_bruta = medir_fuerza_bruta(valores)

        tiempo_divide, suma_divide = medir_divide_venceras(valores)

        assert suma_bruta == suma_divide

        tiempos_fuerza_bruta.append(tiempo_bruta)
        tiempos_divide_venceras.append(tiempo_divide)

        print(
            f"n={n} | "
            f"Fuerza bruta={tiempo_bruta:.6f} s | "
            f"Divide y venceras={tiempo_divide:.6f} s"
        )

    plt.figure()

    plt.plot(
        TAMANOS,
        tiempos_fuerza_bruta,
        marker="o",
        label="Fuerza bruta",
    )

    plt.plot(
        TAMANOS,
        tiempos_divide_venceras,
        marker="o",
        label="Divide y venceras",
    )

    plt.title("Tiempo de ejecucion vs tamaño de entrada")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo promedio (segundos)")
    plt.legend()
    plt.grid()

    plt.savefig(
        "graficas/tiempo_vs_n.png",
        bbox_inches="tight",
    )

    plt.close()

    print("\nGrafica generada correctamente.")


if __name__ == "__main__":
    main()
