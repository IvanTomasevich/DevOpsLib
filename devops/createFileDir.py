"""
Este script tine como objetivo crear un directorio o un archivo validando si existe
No tiene dependencias y es importado de cualquier script que necesite verificar si
existe y crear un directorio o un archivo cualquiera sea sue extensión.
"""
import os


def directory_create(mkdir):
    """
    This function creates a directory if it does not exist.
    :param mkdir: str Full path.
    :return: message if it was created or already exists.
    """
    if not os.path.exists(mkdir):
        os.mkdir(mkdir)
        print(f"Creating dir '{mkdir}'")
    else:
        print(f"The '{mkdir}' dir already exist")
    return mkdir


def file_create(path, file, content):
    """
    Esta función crea un archivo si no existe.
    :param path: Path where to create the file.
    :param file: File name and extension to create.
    :param content: Content that you intend to write to the file.
    :return: message if it was created or already exists.
    """
    file_path = os.path.join(path, file)
    if not os.path.isfile(file_path):
        with open(file_path, "w") as f:
            f.write(content)
        print(f"The file '{file}' was created")
        return file
    else:
        print(f"The '{file}' file already exists")
        return file
