"""
Este script tine como objetivo crear un directorio o un archivo validando si existe
No tiene dependencias y es importado de cualquier script que necesite verificar si
existe y crear un directorio o un archivo cualquiera sea sue extensión.
"""
import os


def directory_create(mkdir):
    """
    Esta función crea un directorio si no existe
    :param mkdir: str del path completo
    :return: mensaje si fue creado o ya existe
    """
    if not os.path.exists(mkdir):
        os.mkdir(mkdir)
        print(f"Creando el directorio {mkdir}")
    else:
        print(f"El directorio {mkdir} ya existe")
    return mkdir


def file_create(path, file, content):
    """
    Esta función crea un archivo si no existe
    :param path: path donde se va a crear el archivo
    :param file: nombre del archivo y extensión a crear
    :param content: contenido que se pretende escribir en el archivo
    :return: mensaje si fue creado o no
    """
    file_path = os.path.join(path, file)
    if not os.path.isfile(file_path):
        with open(file_path, "w") as f:
            f.write(content)
        print(f"El archivo {file} fue creado")
        return file
    else:
        print(f"El directorio {file} ya existe")
        return file
