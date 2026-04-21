from .conexionDB import ConexionDB
from tkinter import messagebox


#funcion para crear la tabla en la bd sqlite
def crearTabla():
    conexion=ConexionDB()

    sql="""
            CREATE TABLE peliculas(
                idPelicula INTEGER,
                nombre VARCHAR(100),
                duracion Varchar(10),
                genero VARCHAR(100),
                PRIMARY KEY(idPelicula AUTOINCREMENT)
            )

        """
    
    try:
        #ejecutamos el sql con el cursor
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        titulo="Crear Registro"
        mensaje="Secreo la tabla en la base de datos"
        messagebox.showinfo(titulo,mensaje)
    except:
        titulo="Crear Registro"
        mensaje="La tabla ya está creada"
        messagebox.showwarning(titulo,mensaje)

def borrarTabla():
    conexion=ConexionDB()
    sql= "DROP TABLE peliculas"

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        titulo="Borrar Registro"
        mensaje="La tabla de la base de datos se borro con éxito"
        messagebox.showinfo(titulo,mensaje)
    except:
        titulo="Crear Registro"
        mensaje="No hay tabla para borrar"
        messagebox.showerror(titulo,mensaje)



#clase para registrar peliculas
class Pelicula:
    def __init__(self,nombre,duracion,genero) -> None:
        self.idPelicula=None
        self.nombre=nombre
        self.duracion=duracion
        self.genero=genero

    #El método especial __str__ en Python sirve para definir cómo quieres que se vea tu objeto cuando alguien lo imprima (usando print()) o lo convierta a una cadena de texto (usando str()).
    def __str__(self) -> str:
        return f"Película: [{self.nombre} - Duración:{self.duracion} - Género: {self.genero}]"


def guardarPelicula(pelicula):
    conexion=ConexionDB()
    sql=f"""
        INSERT INTO peliculas (nombre,duracion,genero)
        VALUES ('{pelicula.nombre}','{pelicula.duracion}','{pelicula.genero}')
    """

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
    except:
        titulo="Conexión al Registro"
        mensaje="La tabla peliculas no está creada en la base de datos"
        messagebox.showerror(titulo,mensaje)