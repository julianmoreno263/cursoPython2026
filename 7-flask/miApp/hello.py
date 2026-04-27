from flask import Flask, render_template


#para correr la aplicacion en flask se usa este comando: flask --app "nombre aplicacion" --debug run, el modo --debug lo que hace es depurar, si hay errores en la app este modo los marca,y cada vez que haya un cambio en la app no hay que estar corriendo de nuevo la aplicacion,ella se reinicia automaticamente


#creamos aplicacion flask
app=Flask(__name__)

#creamos la ruta principal la cual debe ir asociada a una funcion, estas funciones representan las vistas de la aplicacion. Una vista puede tener varias rutas,por ejemplo la pagina principal puede tener la ruta "/" y la ruta     "/index". Con render_template renderizo las plantillas, tambien se pueden pasar parametros para mostrarlos desde la plantilla,en la plantilla html se reciben utilizando {{}}
@app.route("/")
@app.route("/index")
def index():
    name="Julian"
    return render_template("index.html", name=name)


#las rutas pueden recibir parametros,se los indicamos en la ruta entre <>, y la funcion llevaria el parametro para poder usarlo. Tambien se pueden recibir diferentes tipos de parametros no solo string,tambiem int,float,etc,simplemente le indicamos el tipo de parametro. Como una funcion puede tener varias rutas podemos evaluar si una ruta tiene parametros o no y actuar en consecuencia asi:
@app.route("/hello")
@app.route("/hello/<name>")
@app.route("/hello/<name>/<int:age>")
def hello(name=None,age=None):
    if name==None and age==None:
        return f"<h1>Hola mundo<h1/>"
    elif age==None:
        return f"<h1>Hola {name}<h1/>"
    else:
        return f"<h1>Hola {name}, tu edad es {age} años<h1/>"


#la funcion escape de la libreria de flask markupsafe sirve para escapar codigo que podria ser dañino para la aplicacion,por ejemplo en la url nos podrian inyectar codigo de javascript para vulnerar la aplicacion,entonces escape ayuda a que este codigo dañino no se ejecute sino que se muestre como un simple string. En la ruta se puede utilizar la etiqueta <code> para inyectar codigo, si no queremos que ese codigo se ejecute al visitar esa ruta lo escapamos con la funcion escape(), aqui en este caso el codigo que pasemos solo se mostrara como un string y no se ejecuta
from markupsafe import escape
@app.route("/code/<path:code>")
def code(code):
    return f"<code>{escape(code)}</code>"

    