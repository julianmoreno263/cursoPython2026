from flask import Blueprint,render_template

# 1. Definimos el Blueprint
bp=Blueprint("auth",__name__,url_prefix="/auth")

#2-creamos las vistas que despues se importaran en __init__.py
@bp.route("/register")
def register():
    return render_template("auth/register.html")

@bp.route("/login")
def login():
    return render_template("auth/login.html")

@bp.route("/profile")
def profile():
    return "Página de perfil"