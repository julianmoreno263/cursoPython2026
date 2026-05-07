from flask import Blueprint

# 1. Definimos el Blueprint
bp=Blueprint("auth",__name__,url_prefix="/auth")

#2-creamos las vistas que despues se importaran en __init__.py
@bp.route("/register")
def register():
    return "Página de registro"


@bp.route("/login")
def login():
    return "Página de login"

@bp.route("/profile")
def profile():
    return "Página de perfil"