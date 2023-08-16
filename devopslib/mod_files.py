"""
Este script modifica específicamente archivos.
Por un lado, puede modificar contenido y también agregar.
También si ese archivo está dentro de un zip se puede extraer
y volver a insertar en
"""

import fileinput
import os
import subprocess
import zipfile


def replace_content(input_file, replacements):
    """
    Busca un contenido en un archivo y lo reemplaza por otro.
    :param input_file: Str Nombre del archivo a modificar
    :param replacements: Diccionario Str: Key= lo que tienes que modificar por Value= la modificación
    :return: Imprime un mensaje
    """
    # Leo linea por linea del archivo
    for line in fileinput.input(input_file, inplace=True):
        # Busco la línea exacta que quiero reemplazar y reemplazo
        for search_for in replacements:
            replace_with = replacements[search_for]
            line = line.replace(search_for, replace_with)
        print(line, end='')


def add_content(input_file, output_file, replacements):
    """
    Busca un contenido en un archivo y agrega nuevo a continuación.
    :param input_file: Str Nombre del archivo a agregar contenido.
    :param output_file: Diccionario Str: Key= Texto a buscar Value= Texto a agregar
    :param replacements:
    :return:
    """
    # Abro los archivos para trabajarlos
    with open(input_file) as in_file, open(output_file, 'w') as out_file:
        # Recorro las líneas del archivo
        for line in in_file:
            # Busco la coincidencia y agrego lo nuevo a continuación y escribo el archivo nuevo
            for search_phrase, replace_phrase in replacements.items():
                if line.strip() == search_phrase:
                    out_file.write(replace_phrase + '\n')
                    break
            else:
                out_file.write(line)
        # Borro el archivo original y renombro el nuevo con el nombre del anterior
        os.remove(input_file)
        os.rename(output_file, input_file)


def unzip_file(zip_file, file):
    """
    Saca un archivo de un .zip
    :param zip_file: Str Nombre del archivo .zip
    :param file: Str Nombre del archivo a sacar del .zip
    :return:
    """
    # Abro el archivo .zip
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        # Extraigo el archivo que quiero
        zip_ref.extract(file)


def add_file_to_zip(zip_file, file):
    """
    Agrega un archivo a un .zip ya existente, puede ser un
    archivo dentro de un folder pero se debe tener la copia
    del path con el archivo a agregar.
    :param zip_file: Str Nombre el archivo .zip
    :param file: Str Nombre del archivo a agregar al .zip
    :return:
    """
    # Comando jar u para agregar contenido en un zip
    subprocess.run(["jar", "uf", zip_file, file])
