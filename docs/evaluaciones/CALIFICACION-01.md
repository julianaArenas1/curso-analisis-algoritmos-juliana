# Retroalimentación — Fundamentos, complejidad y recurrencias

**Estudiante:** Juliana Arenas Arias · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `83dc53b`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 25 |
| Calidad de la explicación teórica | 16 / 25 |
| Corrección de la implementación | 16 / 20 |
| Calidad del análisis de las gráficas | 17 / 20 |
| Documentación y organización del informe | 8 / 10 |
| **Total** | **76 / 100** |
| **Nota (0–5)** | **3.80** |

## 1. Corrección conceptual (19 / 25)
**Lo que hizo bien:**
- Distingue entre que el resultado sea correcto y que llegue a tiempo, y nombra la ventana de cuatro horas como lo que se incumple.
- Explica que un servidor más rápido solo ayuda un rato porque el trabajo crece mucho al crecer los datos.
- Da un segundo ejemplo propio (matrículas de una universidad) con cantidad de datos y tiempo límite.
- Relaciona más horas de proceso con más energía acumulada día tras día, y explica que el orden de la lista decide a quién se llama primero.

**Lo que puede mejorar:**
- Dice que los pacientes y el personal del centro de contacto se ven afectados, pero no responde con claridad quién asume el costo de cada error ni da un caso concreto de una persona perjudicada.
- La parte ambiental se queda en lo general: no relaciona el tiempo del proceso con el consumo de energía de forma más precisa.

## 2. Calidad de la explicación teórica (16 / 25)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)`, explica cada término y lo resuelve con el árbol de recursión: niveles, costo por nivel y resultado `Θ(n log n)`.
- Escribe la predicción antes de medir y explica por qué el peor caso importa para la ventana estricta.
- Incluye la tabla de complejidades de los dos algoritmos.

**Lo que puede mejorar:**
- Al definir mejor caso, peor caso y caso promedio, no dice sobre qué conjunto de entradas (de tamaño `n` fijo) se toma el mínimo, el máximo o el promedio.
- El análisis de insertion sort no se hace línea a línea: falta indicar cuántas veces se ejecuta cada línea de su código y sumar los costos.
- El árbol de recursión se describe con palabras; hacía falta dibujarlo (por ejemplo, en texto dentro de un bloque de código).

## 3. Corrección de la implementación (16 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien de mayor a menor, no cambian la lista original y cuentan comparaciones entre elementos (una lista ya ordenada da exactamente `n - 1`).
- `merge_sort` tiene su propia mezcla recursiva y no se usa `sorted()` ni `list.sort()`.
- Los generadores dan listas de `n` valores distintos, con semilla y con el escenario B bien armado (98 % ordenado y 2 % al final).
- Las funciones tienen `type hints` y *docstrings* con formato Google.

**Lo que puede mejorar:**
- No se cumple del todo PEP 8: los imports en `parte3_casos.py` y `parte4_complejidad.py` quedan después de código.
- `generar_casi_ordenado` falla con `n = 0`, y a `medir_escenario` y `medir_tiempo` les falta indicar el tipo del parámetro que recibe una función.

## 4. Calidad del análisis de las gráficas (17 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, tienen título, ejes con nombre y leyenda, y muestran las curvas pedidas en los mismos ejes.
- Identifica con cifras el peor caso (C), el mejor (B) y el intermedio (A), y lo contrasta con su predicción.
- En 4.3 recomienda merge sort, justifica que sirve sin importar cómo lleguen los datos, estima las 11,64 horas de insertion sort y los 4,78 segundos de merge sort declarando que es una estimación, y responde a la propuesta del servidor con ese dato.
- Menciona la memoria adicional de merge sort.

**Lo que puede mejorar:**
- No explica qué pasa con los tamaños pequeños, donde las curvas están casi pegadas.
- La estimación usa el tiempo de 1,19 s de la Parte 4, pero en la Parte 3 el mismo escenario A dio 2,67 s con `n = 6400`; conviene explicar esa diferencia entre mediciones.
- La respuesta sobre el servidor debería citar de forma explícita la gráfica de donde sale el dato.

## 5. Documentación y organización del informe (8 / 10)
**Lo que hizo bien:**
- Siguió la estructura de carpetas y los nombres de archivos acordados, con las gráficas incrustadas y visibles.
- Incluye instrucciones para reproducir y enlaza el código en la Parte 3.
- Hizo seis commits con mensajes claros para este laboratorio.

**Lo que puede mejorar:**
- La Parte 4 no enlaza `parte4_complejidad.py`, que es lo que pide el informe.

## ¿El código funciona?
Sí. Los dos algoritmos ordenan bien y los scripts corren sin errores y generan las tres gráficas.

## Para el próximo laboratorio
- Defina cada caso (mejor, peor, promedio) diciendo sobre qué entradas y de qué tamaño se toma.
- Cuando se pida un análisis línea a línea, escriba cuántas veces se ejecuta cada línea y sume.
- Para cada perjuicio, diga claramente quién asume el costo.
- Enlace el código de cada parte práctica y corra `pycodestyle` antes de entregar.
- Cuando dos mediciones del mismo caso difieran, explíquelo en el informe.
