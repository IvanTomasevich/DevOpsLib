import os
import pytest
from create_file_dir import directory_create, file_create


# Fixture para crear y limpiar el directorio de prueba
@pytest.fixture
def test_directory():
    dir_name = "test_directory"
    os.mkdir(dir_name)
    yield dir_name
    os.rmdir(dir_name)


# Prueba para directory_create
def test_directory_create(test_directory):
    result = directory_create(test_directory)
    assert os.path.exists(test_directory)
    assert result == test_directory


# Prueba para file_create
def test_file_create(test_directory):
    file_name = "test_file.txt"
    file_content = "This is a test file."
    result = file_create(test_directory, file_name, file_content)

    file_path = os.path.join(test_directory, file_name)
    assert os.path.isfile(file_path)
    assert result == file_name
