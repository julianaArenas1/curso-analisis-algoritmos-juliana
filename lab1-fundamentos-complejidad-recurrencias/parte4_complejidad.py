"""Comparacion experimental entre insertion sort y merge sort."""

import time

import matplotlib

matplotlib.use("Agg")

from matplotlib import pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3


def medir_tiempo(algoritmo, datos: list[int]) -> float:
    """Mide el tiempo promedio de ejecucion de un algoritmo.

    Args:
        algoritmo: algoritmo de ordenamiento que se va a medir.
        datos: lista con los datos de entrada.

    Returns:
        Tiempo promedio de ejecucion en segundos.
    """
    tiempos = []

    for _ in range(REPETICIONES):
        inicio = time.perf_counter()

        algoritmo(datos)

        fin = time.perf_counter()

        tiempos.append(fin - inicio)

    return sum(tiempos) / len(tiempos)


def main() -> None:
    """Compara insertion sort y merge sort con datos aleatorios."""
    tiempos_insertion = []
    tiempos_merge = []

    for n in TAMANOS:
        datos = generar_aleatorio(n)

        tiempo_insertion = medir_tiempo(
            insertion_sort,
            datos,
        )

        tiempo_merge = medir_tiempo(
            merge_sort,
            datos,
        )

        tiempos_insertion.append(tiempo_insertion)
        tiempos_merge.append(tiempo_merge)

        print(
            f"n={n} | "
            f"Insertion={tiempo_insertion:.6f} s | "
            f"Merge={tiempo_merge:.6f} s"
        )

    plt.figure()

    plt.plot(
        TAMANOS,
        tiempos_insertion,
        marker="o",
        label="Insertion Sort",
    )

    plt.plot(
        TAMANOS,
        tiempos_merge,
        marker="o",
        label="Merge Sort",
    )

    plt.title("Tiempo de Insertion Sort vs Merge Sort")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo promedio (segundos)")
    plt.legend()
    plt.grid()

    plt.savefig(
        "graficas/parte4_tiempo.png",
        bbox_inches="tight",
    )

    plt.close()

    print("\nGrafica generada correctamente.")


if __name__ == "__main__":
    main()