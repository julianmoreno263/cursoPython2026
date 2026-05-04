#archivo para la autenticacion de usuario, aqui tambien utilizamos blueprint

from flask import Blueprint, render_template
from . import models  #con esta linea se migran los modelos para la bd

#instancia de blueprint,este es el prefijo para las demas rutas
bp=Blueprint("auth",__name__,url_prefix="/auth")


#ruta /list
@bp.route("/register")
def register():
    return render_template("auth/register.html")

#ruta /create
@bp.route("/login")
def login():
        return render_template("auth/login.html")
