#configuraciones iniciales de la app

from flask import Flask, render_template
from . import todo
from . import auth


#creamos una funcion que crea la app, esta funcion nos permitira reutilizarla donde la necesitemos,por ejemplo  cuando necesitemos usar la bd con una instancia de la aplicacion podemos reutilizar esta funcion 



def create_app():
    #creamos app
    app=Flask(__name__)
    #configuracion del proyecto
    app.config.from_mapping(
        DEBUG=True,
        SECRET_KEY="dev"
    )

    #registrar blueprint
    app.register_blueprint(todo.bp)
    app.register_blueprint(auth.bp)



    @app.route("/")
    def index():
        return render_template("index.html")
    
    return app
    