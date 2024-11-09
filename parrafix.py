import re
import argparse

def process_text(text):
    # Expresión 1: Palabras cortadas
    text = re.sub(r'([A-Za-z]+)-\r?\n', r'\1', text)

    # Expresión 2: Números de Referencias
    text = re.sub(r'([a-zA-Z]+\.)(\d+)(\r?\n)', r'\1', text)

    # Expresión 3: Saltos de lineas
    text = re.sub(r'(?<!\.)\r?\n', '\s', text)

    return text

def main():
    # Configurar argparse para recibir argumentos desde la línea de comandos
    parser = argparse.ArgumentParser(description='Procesar texto en un archivo.')
    parser.add_argument('filename', type=str, help='El nombre del archivo a procesar')

    args = parser.parse_args()

    try:
        # Leer el contenido del archivo
        with open(args.filename, 'r', encoding='utf-8') as file:
            text = file.read()

        # Procesar el texto
        processed_text = process_text(text)

        # Guardar el texto procesado en un nuevo archivo
        output_file_name = 'procesado_' + args.filename
        with open(output_file_name, 'w', encoding='utf-8') as output_file:
            output_file.write(processed_text)

        print(f"El texto procesado se ha guardado en '{output_file_name}'.")

    except FileNotFoundError:
        print(f"El archivo '{args.filename}' no se encontró. Por favor, verificá el nombre del archivo e intentá de nuevo.")

if __name__ == "__main__":
    main()
