"""Experimento de mejor, peor y caso promedio de insertion sort."""

import time

import matplotlib

matplotlib.use("Agg")

from matplotlib import pyplot as plt

from algoritmos import insertion_sort
from datos import (
    generar_aleatorio,
    generar_casi_ordenado,
    generar_inverso,
)


TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3


def medir_escenario(
    generador,
    nombre: str,
) -> tuple[list[int], list[int], list[float]]:
    """Mide comparaciones y tiempo para un escenario de Tamiza.

    Args:
        generador: funcion utilizada para generar los datos de prueba.
        nombre: nombre del escenario que se esta midiendo.

    Returns:
        Una tupla con los tamaños, las comparaciones y los tiempos
        promedio obtenidos.
    """
    comparaciones_resultado = []
    tiempos_resultado = []

    for n in TAMANOS:
        datos = generador(n)

        tiempos = []
        comparaciones = 0

        for _ in range(REPETICIONES):
            inicio = time.perf_counter()

            _, comparaciones = insertion_sort(datos)

            fin = time.perf_counter()
            tiempos.append(fin - inicio)

        tiempo_promedio = sum(tiempos) / len(tiempos)

        comparaciones_resultado.append(comparaciones)
        tiempos_resultado.append(tiempo_promedio)

        print(
            f"{nombre} | n={n} | "
            f"comparaciones={comparaciones} | "
            f"tiempo={tiempo_promedio:.6f} s"
        )

    return TAMANOS, comparaciones_resultado, tiempos_resultado


def graficar_comparaciones(resultados: dict) -> None:
    """Genera la grafica de comparaciones para los tres escenarios.

    Args:
        resultados: resultados obtenidos en las mediciones.

    Returns:
        None.
    """
    plt.figure()

    for nombre, datos in resultados.items():
        plt.plot(
            datos["tamanos"],
            datos["comparaciones"],
            marker="o",
            label=nombre,
        )

    plt.title("Comparaciones de insertion sort por escenario")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.legend()
    plt.grid()

    plt.savefig(
        "graficas/parte3_comparaciones.png",
        bbox_inches="tight",
    )

    plt.close()


def graficar_tiempos(resultados: dict) -> None:
    """Genera la grafica de tiempo para los tres escenarios.

    Args:
        resultados: resultados obtenidos en las mediciones.

    Returns:
        None.
    """
    plt.figure()

    for nombre, datos in resultados.items():
        plt.plot(
            datos["tamanos"],
            datos["tiempos"],
            marker="o",
            label=nombre,
        )

    plt.title("Tiempo de insertion sort por escenario")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo promedio (segundos)")
    plt.legend()
    plt.grid()

    plt.savefig(
        "graficas/parte3_tiempo.png",
        bbox_inches="tight",
    )

    plt.close()


def main() -> None:
    """Ejecuta las mediciones y genera las graficas de la Parte 3."""
    resultados = {}

    escenarios = {
        "A - Aleatorio": generar_aleatorio,
        "B - Casi ordenado": generar_casi_ordenado,
        "C - Orden inverso": generar_inverso,
    }

    for nombre, generador in escenarios.items():
        tamanos, comparaciones, tiempos = medir_escenario(
            generador,
            nombre,
        )

        resultados[nombre] = {
            "tamanos": tamanos,
            "comparaciones": comparaciones,
            "tiempos": tiempos,
        }

    graficar_comparaciones(resultados)
    graficar_tiempos(resultados)

    print("\nGraficas generadas correctamente.")


if __name__ == "__main__":
    main()