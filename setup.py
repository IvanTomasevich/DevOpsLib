from setuptools import setup, find_packages

# Información de la librería
LIBRARY_NAME = 'devopslib'
VERSION = '0.1'
DESCRIPTION = 'Una librería genial para reutilizar y actualizar globalmente código'
AUTHOR = 'Iván Tomasevich'
AUTHOR_EMAIL = 'ivantomasevich@pm.me'
URL = 'https://github.com/IvanTomasevich/DevOpsLib'
LICENSE = 'GPL-3.0'

# Cargar el contenido del README como descripción larga
with open('README.md', 'r', encoding='utf-8') as readme_file:
    LONG_DESCRIPTION = readme_file.read()

setup(
    name=LIBRARY_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=find_packages(),
    install_requires=[
        # Dependencias de tu librería, si las hay
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
