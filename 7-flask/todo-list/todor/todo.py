#archivo para las vistas de la aplicacion, utilizamos Blueprint para organizarlas, estas vistas con blueprint se deben de registrar en el archivo de configuracion __init__.py
from flask import Blueprint

#instancia de blueprint,este es el prefijo para las demas rutas
bp=Blueprint("todo",__name__,url_prefix="/todo")


#ruta /list
@bp.route("/list")
def index():
    return "Lista de tareas"

#ruta /create
@bp.route("/create")
def create():
    return "Crear tarea"