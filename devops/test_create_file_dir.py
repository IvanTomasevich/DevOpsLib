import os
import tempfile
import shutil

from create_file_dir import directory_create, file_create


# Prueba de creación de un directorio
def test_directory_create():
    temp_dir = tempfile.mkdtemp()  # Crea un directorio temporal
    test_dir = os.path.join(temp_dir, "test_directory")

    # Verifica que el directorio no exista inicialmente
    assert not os.path.exists(test_dir)

    # Llama a la función para crear el directorio
    created_dir = directory_create(test_dir)

    # Verifica que el directorio haya sido creado
    assert os.path.exists(created_dir)
    assert os.path.isdir(created_dir)

    # Llama a la función nuevamente para verificar que el directorio ya existe
    created_dir = directory_create(test_dir)

    # Verifica que se indique que el directorio ya existe
    assert os.path.exists(created_dir)
    assert os.path.isdir(created_dir)

    # Limpia el directorio temporal
    shutil.rmtree(temp_dir)


# Prueba de creación de un archivo
def test_file_create():
    temp_dir = tempfile.mkdtemp()  # Crea un directorio temporal
    test_file_path = os.path.join(temp_dir, "test_file.txt")
    test_content = "Este es el contenido de prueba."

    # Verifica que el archivo no exista inicialmente
    assert not os.path.exists(test_file_path)

    # Llama a la función para crear el archivo
    created_file = file_create(temp_dir, "test_file.txt", test_content)

    # Verifica que el archivo haya sido creado
    assert os.path.exists(created_file)
    assert os.path.isfile(created_file)

    # Abre el archivo y verifica su contenido
    with open(created_file, "r") as f:
        content = f.read()
    assert content == test_content

    # Llama a la función nuevamente para verificar que el archivo ya existe
    created_file = file_create(temp_dir, "test_file.txt", test_content)

    # Verifica que se indique que el archivo ya existe
    assert os.path.exists(created_file)
    assert os.path.isfile(created_file)

    # Limpia el directorio temporal
    shutil.rmtree(temp_dir)


if __name__ == "__main__":
    test_directory_create()
    test_file_create()
    print("Todas las pruebas han pasado con éxito.")
