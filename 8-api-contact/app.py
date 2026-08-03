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
    #capturamos los contactos en una lista
    contacts=Contact.query.all()
    
    #recorremos esa lista serializando cada objeto recorrido,los vamos poniendo en un diccionario y los formateamos a json todo en una linea
    return jsonify({"contacts":[contact.serialize() for contact in contacts]})



#ruta para traer un contacto,lo hacemos por su id
@app.route("/contact/<int:id>", methods=["GET"])
def get_contact(id):
    #capturamos los contactos en una lista
    contact=Contact.query.get(id)
    if not contact:
         return jsonify({"message":"El contacto no existe en la base de datos"}),404
    
    #si encuentra el contacto lo devolvemos ya como un json
    return jsonify(contact.serialize())




#ruta para crear un contacto en la bd, esta ruta se prueba en postman, creamos el objeto json en postman y desde ahi lo enviamos para probar la api,en postman vamos a body,raw,en el cuadro azul que dice text seleccionamos json y en el cuadro grande escribimos nuestro objeto json(en postman los json deben de ir con comillas dobles y el ultimo elemento no tiene coma.)
@app.route("/create", methods=["POST"])
def create_contact():
    #creamos un objeto de tipo json y lo utilizamos para crear el objeto de tipo Contact y pasarle los datos
    data=request.get_json()
    contact=Contact(name=data["name"],email=data["email"],phone=data["phone"]) # type: ignore
    #guardamos en la bd el contacto
    db.session.add(contact)
    db.session.commit()
    #retornamos un mensaje, el contacto y el codigo de estado ok(201)
    return jsonify({"message":"Contacto creado con exito", "contact":contact.serialize()}),201



#ruta para editar un registro especifico, podemos utilizar el metodo put o el patch
@app.route("/edit/<int:id>", methods=["PUT","PATCH"])
def edit_contact(id):
    #capturamos el contacto en una lista
    contact=Contact.query.get(id)
    #capturamos el objeto json,osea lo que el cliente nos envia
    data=request.get_json()

    #validamos los datos
    if "name" in data:
        contact.name=data["name"] # type: ignore
    if "email" in data:
        contact.email=data["email"] # type: ignore
    if "phone" in data:
        contact.phone=data["phone"] # type: ignore
    
    #guardamos cambios en la bd 
    db.session.commit()

    return jsonify({"message":"Contacto actualizado con exito", "contact":contact.serialize()}),200 # type: ignore




#ruta para eliminar un registro especifico
@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_contact(id):
    #capturamos los contactos en una lista
    contact=Contact.query.get(id)
    if not contact:
         return jsonify({"message":"El contacto no existe en la base de datos"}),404
    
    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message":"Contacto eliminado con exito"})




# Esto asegura que el servidor corra en modo debug cuando ejecutas el archivo directamente
if __name__ == "__main__":
    app.run(debug=True)