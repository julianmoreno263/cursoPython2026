from os import error
from flask import Blueprint,render_template,request,url_for,redirect,flash,session,g
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from blogr import db
import functools

# 1. Definimos el Blueprint
bp=Blueprint("auth",__name__,url_prefix="/auth")

#2-creamos las vistas que despues se importaran en __init__.py
@bp.route("/register",methods=("GET", "POST"))
def register():

    #si el metodo es post capturamos los datos del formulario de registro
    if request.method=="POST":
        username=request.form.get("username")
        email=request.form.get("email")
        password=request.form.get("password")

        #construimos un objeto de tipo User
        user=User(username,email,generate_password_hash(password)) # type: ignore

        #validamos los datos
        error=None

        #comparamos el usuario que queremos registrar con los que esten en la bd por medio del email,si no esta en la bd lo agrega
        user_email=User.query.filter_by(email=email).first()
        if user_email==None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            error=f"El correo {email} ya está registrado en la base de datos"
        flash(error)

    return render_template("auth/register.html")



@bp.route("/login",methods=("GET", "POST"))
def login():
     #si el metodo es post capturamos los datos del formulario de registro
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")

        #validamos datos buscando por email
        error=None
        user=User.query.filter_by(email=email).first()
        if user==None or not check_password_hash(user.password,password): # type: ignore
            error="Correo o contraseña incorrecta"

        #iniciando sesion
        if error is None:
            session.clear()
            session["user_id"]=user.id  # type: ignore
            return redirect(url_for("post.posts"))
        flash(error)

    return render_template("auth/login.html")


#vista para mantener la sesion de un usuario
@bp.before_app_request
def load_logged_in_user():
    user_id=session.get("user_id")

    if user_id==None:
        g.user=None
    else:
        g.user=User.query.get_or_404(user_id)

#vista para cerrar la sesion
@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home.index"))


#decorador para que le inicio de sesion sea obligatorio en la vista donde lo estipulemos
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return wrapped_view





@bp.route("/profile")
def profile():
    return "Página de perfil"