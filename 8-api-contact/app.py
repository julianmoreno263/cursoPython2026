#en este ejercicio crearemos la api en un solo archivo,dependiendo lo que se necesite hacer tambien se puede modularizar. Para crear una api con flask debemos utilizar flask y sqlalchemy

#NOTA: para correr nuestra app usamos: flask --app app --debug run, pero como me estaba apareciendo el debug off,osea el servidor de la app no estaba recargandose automaticamente al hacer un cambio,entonces coloco este codigo: 

#if __name__ == "__main__":
    # app.run(debug=True)

#y para ejecutar la app uso python app.py y ya me activa el debug y asi al realizar un cambio ya lo carga automaticamente en el navegador.

from flask import Flask,request,jsonify 
from flask_sqlalchemy import SQLAlchemy

#creamos la instancia de flask.  
app=Flask(__name__)

#configuramos la url de la bd que vamos a usar
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///contacts.db"

#creamos la instancia de la bd con sqlalchemy
db=SQLAlchemy(app)

#crear modelo de la bd
class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(50),nullable=False)
    phone=db.Column(db.String(11),nullable=False)

    #creamos un metodo para serializar el objeto que creemos de esta clase,asi al serializarlo en forma de diccionario podremos convertirlo facilmente a formato json
    def serialize(self):
        return{
            "id":self.id,
            "name":self.name,
            "email":self.email,
            "phone":self.phone
        }


#crea las tablas en la bd(las migra)
with app.app_context():
    db.create_all()


#crear rutas

#para probar las rutas de la api utilizamos postman,en el navegador podemos probar que la ruta con get funciona,pero ya con post o update no lo podemos hacer de forma directa,asi que utilizamos postman

# Ruta raíz para verificar que la API está viva
@app.route("/", methods=["GET"])
def home():
    return "¡Mi API de Flask con SQLite está funcionando! Página principal"

#ruta para traer los contactos
@app.route("/contacts", methods=["GET"])
def get_contacts():
    return "Lista de contactos"

#ruta para crear un contacto en la bd
@app.route("/create", methods=["POST"])
def create_contact():
    return "Se creo un contacto nuevo"






# Esto asegura que el servidor corra en modo debug cuando ejecutas el archivo directamente
if __name__ == "__main__":
    app.run(debug=True)