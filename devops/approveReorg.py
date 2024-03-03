"""
Este scrip tiene como objetivo aprobar una reorg más guardar una copia con el TAG para mostrar
"""
import datetime
import os
import shutil

from getEnvVars import kb_path, env_path, workspace, build_id
from createFileDir import directory_create

# Guardo los nombres de las reorg .sql
reorg = "ReorganizationScript.sql"
appr_reorg = "ApprovedReorg.sql"

# Guardo variables fecha y hora más la formateo
now = datetime.datetime.now()
fecha_hora = now.strftime("%d-%m-%Y_%H-%M-%S")

path_build = f"{workspace}/ReorgScripts_TAG"
path_fechas = f"{kb_path}/ReorgScripts_DATE"
working_dir = f"{kb_path}/{env_path}/web"

# LLamo a create_dir para almacenar las reorg, si no existe las crea
directory_create(path_build)
directory_create(path_fechas)

# Me paro en el directorio donde están las Reorg
os.chdir(working_dir)

# Si existe el viejo lo elimino
if os.path.exists(appr_reorg):
    os.remove(appr_reorg)
# Copio el SQL con el Build y Fecha en sus path destino si existe
if os.path.exists(reorg):
    shutil.copy(reorg, f"{path_build}/#{build_id}_ReorganizationScript.sql")
    shutil.copy(reorg, f"{path_fechas}/ReorganizationScript_{fecha_hora}.sql")
    print("### Copias de la Reorg OK ###")
    # Renombro el SQL original con el de aprobado
    os.rename(reorg, appr_reorg)
    print("### Reorganización aprobada ###")
else:
    print("### No existe una Reorg pendiente para procesar ###")
