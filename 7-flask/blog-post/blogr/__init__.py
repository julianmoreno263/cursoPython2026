from flask import Flask
from blogr import home,auth,post


#Este código define lo que en el mundo de Flask se conoce como una Application Factory (Fábrica de Aplicaciones).

# En lugar de crear la instancia de app de forma global en el cuerpo de tu archivo, la encapsulas dentro de una función. Esto es una práctica profesional recomendada para proyectos que escalan.

#Declara la función constructora. Al llamarla, esta "fabrica" y te devuelve una instancia lista de tu servidor.
def createApp():

    #crear app de flask, El argumento __name__ le dice a Flask dónde buscar recursos como plantillas y archivos estáticos.
    app=Flask(__name__)

    #registrar vistas, estás diciéndole a la aplicación principal: "Oye, todas las rutas y funciones que definí en el Blueprint llamado 'home', o 'auth',etc, ahora forman parte de esta app".
    app.register_blueprint(home.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(post.bp) # type: ignore


        
    return app