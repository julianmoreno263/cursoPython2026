#archivo para la autenticacion de usuario, aqui tambien utilizamos blueprint,flash sirve para enviar mensajes a nuestras plantillas,como errores,etc. Con werzeug tenemos funcionalidad para encriptar los passwords y poder validar los datos. El objeto g que importamos de flask sirve para almacenar la cookie de sesion

from flask import (Blueprint, render_template,request,url_for,redirect,flash,session,g)
from werkzeug.security import generate_password_hash,check_password_hash
from .models import User  #con esta linea se migran los modelos para la bd
from todor import db

#instancia de blueprint,este es el prefijo para las demas rutas
bp=Blueprint("auth",__name__,url_prefix="/auth")


#ruta /list
@bp.route("/register", methods=("GET","POST"))
def register():
    #1-si usamos POST se deben capturara los datos del formulario primero
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        #2-ahora creamos un objeto de tipo User con el password encriptado
        user=User(username,generate_password_hash(password))
        #3-verificamos si nuestro username ya existe en la bd o no, si no existe lo agregamos a la bd, con session.commit() se guardan los datos, y luego hacemos que se redireccione al login
        user_name=User.query.filter_by(username=username).first()
        if user_name==None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
             error=f"El usuario {username} ya está registrado en la base de datos"

        flash(error)
          

    return render_template("auth/register.html")

#ruta /create
@bp.route("/login", methods=("GET", "POST"))
def login():
        #1-si usamos POST se deben capturar los datos del formulario primero
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]

        error=None
        #2-validamos datos
        user=User.query.filter_by(username=username).first()
        if user == None:
            error="Nombre de usuario incorrecto"
        elif not check_password_hash(user.password, password):
            error="Contraseña incorrecta"
        #3-iniciar sesion
        if error is None:
            session.clear()
            session['user_id']=user.id # type: ignore
            return redirect(url_for("todo.index"))

        flash(error)
    return render_template("auth/login.html")


#funcion para capturar el usuario que ha iniciado sesion por medio del id para poder mantener la sesion,con el decorador le indicamos que se ejecute en cada peticion,en cualquier parte de la aplicacion verifica si alguien ha iniciado sesion o no, con esto se mantiene el inicio de sesion
@bp.before_app_request
def loadLoggedUser():
    #capturamos el usuario que ha iniciado sesion
    user_id=session.get('user_id')
    #si nadie ha iniciado sesion user_id sera None,si alguien inicio sesion capturamos el id de ese usuario o sino devolvemos un error 404
    if user_id is None:
        g.user=None
    else:
        g.user=User.query.get_or_404(user_id)


#funcion para cerrar sesion
@bp.route("/logout") # type: ignore
def logout():
    session.clear()
    return redirect(url_for("index"))