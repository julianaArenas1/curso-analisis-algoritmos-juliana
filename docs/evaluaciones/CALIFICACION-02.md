# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Juliana Arenas Arias · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `c0b72de`

Muy buen trabajo: el código es correcto y el informe está bien organizado.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 17 / 20 |
| Calidad de la explicación teórica | 19 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 20 / 25 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **89 / 100** |
| **Nota (0–5)** | **4.45** |

## 1. Corrección conceptual (17 / 20)
**Lo que hizo bien:**
- En la pregunta 4 compara bien con el máximo de un arreglo: la recurrencia `T(n) = 2T(n/2) + Θ(1)` da `Θ(n)`, igual que un solo recorrido, y concluye que dividir no mejora nada.
- En la pregunta 5 recomienda divide y vencerás, estima los dos tiempos para 1.000.000 de registros sin regla de tres lineal y dice que es una estimación.

**Lo que puede mejorar:**
- En la pregunta 3 dice que divide y vencerás gana desde `n = 100`, pero esto no se puede leer en su gráfica. Faltó una tabla con los tiempos medidos que respaldara esa afirmación.
- En la pregunta 4 faltó decir explícitamente que combinar las dos mitades del máximo cuesta solo una comparación y por eso no hay ganancia.

## 2. Calidad de la explicación teórica (19 / 20)
**Lo que hizo bien:**
- Explica de dónde sale cada término de `T(n) = 2T(n/2) + Θ(n)` y la resuelve con el método maestro, comparando `f(n)` con `n^(log₂2) = n`.
- Justifica bien el `Θ(n²)` de la fuerza bruta con la suma `n + (n-1) + ... + 1`.

**Lo que puede mejorar:**
- Nombre el caso del método maestro de forma más completa, indicando que se cumple la condición `f(n) = Θ(n^(log_b a))`.

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- Las tres funciones resuelven los tres casos, no llaman a la fuerza bruta y no modifican la lista recibida.
- Las pruebas cubren todos los casos pedidos y 20 listas aleatorias, comparando la suma y no los índices.
- Tiene *type hints* y *docstrings* en las funciones y el código cumple PEP 8.

**Lo que puede mejorar:**
- Las pruebas son una sola secuencia de `assert` sin separar en funciones; es aceptable, pero sería más claro con funciones de prueba.

## 4. Calidad del análisis de las gráficas (20 / 25)
**Lo que hizo bien:**
- La gráfica tiene ambas curvas en los mismos ejes, título, ejes rotulados y leyenda, con siete tamaños (de 10 a 4000).
- Calcula el factor al duplicar `n` para los dos algoritmos y lo compara con `Θ(n²)` y `Θ(n log n)`.

**Lo que puede mejorar:**
- Las cifras del informe para `n = 1000` y `n = 2000` en fuerza bruta (0,031902 y 0,111940) no coinciden con la gráfica publicada, donde se leen cerca de 0,025 y 0,100. Con los valores de la gráfica el factor sería cercano a 4, no 3,51. Las cifras del informe deben salir de la misma corrida que la gráfica.
- Para divide y vencerás faltó indicar cuál sería el factor esperado para esos tamaños con valores concretos.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- Siguió la estructura de carpetas acordada (`lab2-divide-y-vencer/` con todos los archivos), el informe sigue el orden pedido, la gráfica se ve y cada parte enlaza su código.
- Hay cinco commits con mensajes descriptivos.

**Lo que puede mejorar:**
- Las instrucciones de reproducción no dicen que hay que entrar a la carpeta `lab2-divide-y-vencer/` antes de ejecutar los comandos.

## ¿El código funciona?
Sí. Las pruebas pasan, ambos algoritmos dan la misma suma en mis pruebas con listas aleatorias, y `medicion.py` corre y genera la gráfica sin errores.

## Para el próximo laboratorio
- Copie en el informe los números de la misma corrida que generó la gráfica publicada.
- Agregue una tabla de tiempos medidos para respaldar lo que dice de los tamaños pequeños.
- Indique en las instrucciones en qué carpeta se ejecutan los comandos.
- En las preguntas conceptuales, nombre explícitamente el costo de combinar y la condición del método maestro.
