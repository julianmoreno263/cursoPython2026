from flask import Blueprint

# 1. Definimos el Blueprint
bp=Blueprint("post",__name__,url_prefix="/post")

#2-creamos las vistas que despues se importaran en __init__.py
@bp.route("/posts")
def posts():
    return "Página de posts"


@bp.route("/create")
def create():
    return "Página de create"

@bp.route("/update")
def update():
    return "Página de update"