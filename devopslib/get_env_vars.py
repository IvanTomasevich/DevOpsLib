"""
Devuelve variables de entorno de jenkins.
Las variables siempre respetando las normas PEP8.
"""
import os

"""
#### Variables globales de Jenkins ####
"""

# Trae la ruta del proyecto "Proyecto/Pipeline"
job = os.environ.get("JOB_NAME")

# Trae la URL del Pipeline "https://jenkins.accionpoint.com/job/[Proyecto]/job/[Pipeline]/"
build = os.environ.get("BUILD_URL")

# Trae el numero del Build del pipeline "432"
build_id = os.environ.get("BUILD_ID")

# Trae la URL del Job o build con la revisión "https://jenkins.accionpoint.com/job/[Proyecto]/job/[Pipeline]/3556/"
job_url = os.environ.get("JOB_URL")

# Trae el path del workspace de Jenkins
workspace = os.environ.get("WORKSPACE")

"""
#### Variables declaradas en el Jenkins file ####
"""

# Trae el path de la KB
kb_path = os.environ.get("KBPath")

# Trae el nombre del target path para armar la ruta completa donde esta el WEB, DEPLOY, etc.
# (se debe definir en una variable en Jenkins file)
env_path = os.environ.get("envPath")

# Trae el nombre del zip o war del deploy (se debe definir en una variable en Jenkins file)
deploy = os.environ.get("Deploy")

# Trae el appkey del deploy
deploy_appkey = os.environ.get("DeployAppKey")

# Trae el deploy path para realizar update en este
deploy_path = os.environ.get("deployPath")
