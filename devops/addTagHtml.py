"""
Script que se usa para probar el deploy, si se actualiza el DevOps.html
es porque el deploy anda genial y el problema puede ser o el deployment unit
o el archivo <deployment_unit>.gxdproj
Dependencias: createFileDir.py | getEnvVars.py
"""
import datetime
import os
import shutil
import subprocess

from createFileDir import file_create
from getEnvVars import workspace, kb_path, env_path, build_id, deploy, deploy_path

# Guardo variables fecha y hora más la formateo
now = datetime.datetime.now()
date_time = now.strftime("%d-%m-%Y %H-%M-%S")

# Me fijo si existe el archivo DevOps.html, si no lo creo y lo escribo desde DevOps.html
# Defino los argumentos
html = "DevOps.html"
html_path = workspace
template = """<!-- Template desde DevOps -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>DevOps Test Deploy</title>
</head>
<body>
  <h1>Build #TAG | datetime</h1>
</body>
</html>
<!-- Este archivo imprime el número de build y la fecha y hora de su ejecución -->
"""
# with open(html, "r") as f:
#     template = f.read()

# LLamo al createFileDir para crear el archivo arg(path, file, content)
file_create(workspace, html, template)

# Copio el html para actualizar en él .zip
shutil.copy(f'{workspace}/DevOps.html',
            f'{kb_path}/{env_path}/{deploy_path}')


def add_tag_html(job, job_time):
    """
    Add the Pipeline Job TAGS and the date and time to the DevOps file.html
    :param job: str of Jenkins build number
    :param job_time: str of the date and time the build was run
    :return: The DevOps file.html modified with the Build and date and time
    """
    # Lee el archivo HTML
    with open(html, "r") as f_DO:
        contenido = f_DO.read()
    # Reemplaza la palabra "TAG" por la variable de entorno "VARIABLE"
    contenido = contenido.replace("TAG", job)
    contenido = contenido.replace("datetime", job_time)
    # Guarda el archivo HTML actualizado
    with open(html, "w") as f_DO:
        f_DO.write(contenido)


# Me muevo al path de trabajo y archivos a modificar
os.chdir(f'{kb_path}/{env_path}/{deploy_path}')

# Llamo a la func. (subrutina) para pasarle el build id y la fecha y hora del build de Jenkins
add_tag_html(build_id, date_time)

# Actualizo .zip con html con el build id
subprocess.run(["jar", "uf", deploy, html])
# Elimino el html para el próximo proceso
os.remove(html)
