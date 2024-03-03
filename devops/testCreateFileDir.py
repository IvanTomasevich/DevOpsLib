import os
import pytest
from createFileDir import directory_create, file_create

@pytest.fixture
def test_dir(tmpdir):
    return str(tmpdir.mkdir("test_dir"))

def test_directory_create_not_exists(test_dir):
    new_dir = os.path.join(test_dir, "new_dir")
    assert directory_create(new_dir) == new_dir
    assert os.path.isdir(new_dir)

def test_directory_create_exists(test_dir):
    existing_dir = os.path.join(test_dir, "existing_dir")
    os.mkdir(existing_dir)
    with pytest.raises(FileExistsError):
        directory_create(existing_dir)

def test_file_create_not_exists(test_dir):
    new_file = "new_file.txt"
    file_content = "This is a test file."
    file_path = os.path.join(test_dir, new_file)
    assert file_create(test_dir, new_file, file_content) == new_file
    assert os.path.isfile(file_path)
    with open(file_path, "r") as f:
        assert f.read() == file_content

def test_file_create_exists(test_dir):
    existing_file = "existing_file.txt"
    existing_file_content = "Existing file content."
    file_path = os.path.join(test_dir, existing_file)
    with open(file_path, "w") as f:
        f.write(existing_file_content)
    with pytest.raises(FileExistsError):
        file_create(test_dir, existing_file, "New content")
    with open(file_path, "r") as f:
        assert f.read() == existing_file_content
