# Parrafix
Soluciona el error cuando un txt tiene todos los parrafos cortados, con saltos de lineas, los elimina y deja solo si terminan con punto.

Despues de convertir una archivo pdf a txt todas los renglones terminan con saltos de líneas, esto es incorrecto. deberían ser lineas continuas hasta el punto de fin de parrafo.

### Guía: Uso y Función del Script de Procesamiento de Texto

Este archivo adjunto te ayudará a entender para qué sirve el script, qué problemas resuelve y cómo usarlo.

---

## ¿Qué hace este script?

El script está diseñado para procesar texto en un archivo, limpiando y ajustando su formato automáticamente. Está pensado especialmente para casos en los que un archivo de texto tiene problemas comunes como:

- **Palabras divididas por guiones al final de una línea**
- ejemplo: "pro-\ncesar" pro- salto de linea cesar). 
- **Referencias numéricas innecesarias al final de líneas**.
- **Saltos de línea innecesarios que interrumpen el flujo de los párrafos**.

El objetivo principal es mejorar la calidad del texto para que sea más fácil de leer o procesar.

---

## Funciones del script

El script realiza las siguientes transformaciones:

### 1. **Unir palabras cortadas por guiones**
   - Cuando una palabra está dividida entre líneas mediante un guion (`-`), el script elimina el guion y el salto de línea.
   - **Ejemplo**: 
     ```plaintext
     pro-
     cesar
     ```
     Se convierte en:
     ```plaintext
     procesar
     ```

### 2. **Eliminar referencias numéricas**
   - Si una línea termina con un texto seguido de un número (ejemplo: "Texto.123\n"), se elimina el número y el salto de línea.
   - **Ejemplo**:
     ```plaintext
     Sección.123
     ```
     Se convierte en:
     ```plaintext
     Sección.
     ```

### 3. **Eliminar saltos de línea innecesarios**
   - Si un salto de línea no está precedido por un punto (`.`), se reemplaza por un espacio. Esto es útil para unir líneas que deberían formar un solo párrafo.
   - **Ejemplo**:
     ```plaintext
     Esto es un
     párrafo dividido
     en varias líneas.
     ```
     Se convierte en:
     ```plaintext
     Esto es un párrafo dividido en varias líneas.
     ```

---

## ¿Qué problemas resuelve?

El script es útil en situaciones como:
- Archivos de texto generados a partir de documentos escaneados o convertidos de PDF.
- Archivos donde las líneas están mal formateadas debido a divisiones automáticas de palabras.
- Necesidad de limpiar referencias o elementos innecesarios en el texto antes de usarlo para otro propósito, como convertirlo a audio o realizar análisis textual.

---

## ¿Cómo usar el script?

1. Asegurate de tener Python instalado en tu computadora.
2. Guarda el script en un archivo con extensión `.py` (por ejemplo, `parrafix.py`).
3. Desde la línea de comandos, ejecutá el script pasando como argumento el nombre del archivo que querés procesar. Ejemplo:
   ```bash
   python parrafix.py archivo.txt
   ```
4. El script procesará el archivo y generará uno nuevo con el prefijo `procesado_` en el mismo directorio. Por ejemplo, si el archivo original era `archivo.txt`, el resultado será `procesado_archivo.txt`.

---

## Mensajes útiles del script

- **Archivo no encontrado**: Si el archivo no existe, el script te lo indicará y te pedirá que verifiques el nombre del archivo.
- **Texto procesado exitosamente**: Indica que el archivo fue procesado y se guardó correctamente.

---
