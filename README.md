# Parrafix
Soluciona el error cuando un txt tiene todos los parrafos cortados, con saltos de lineas, los elimina y deja solo si terminan co punto.
Despues de conevertir una archivo pdf a txt todas los renglones terminan con saltos de líneas, esto es incorrecto. deberían ser lineas continuas hasta el punto de fin de parrafo.
Este script en python abre un txt y usa las expreciones regulares
-   Palabras cortadas: Buscá saltos cuando la línea termina en guion medio (-) precedido de una o más letras.
     -   Expresión Regular: (\[A-Za-z\]+)-\\r?\\n
     -   Reemplazo: \\1

-   Números de Referencias: Eliminá las referencias a pie de página, números que están después de un punto al final de un renglón.
    -   Expresión Regular: (\[a-zA-Z\]+\\.)(\\d+)(\\r?\\n)
    -   Reemplazo: \\1\\3

-   Saltos de línea: Eliminá los saltos de línea cuando estas no terminen con un punto.
    -   Expresión Regular: (?<!\\.)\\r?\\n
    -   Reemplazo: (Dejá en blanco)


# Articulo de referencia.
[Lo mismo en notepad++](https://www.aldo.net.ar/2024/11/elimina-lineas-cortadas-resultante-de.html)
