import sqlite3

#clase para conectar la bd
class ConexionDB:
    #el constructor crea el archivo peliculas.db si no existe
    def __init__(self) -> None:
        self.db=r"6-proyecto/catalogoPeliculas/catalogo_peliculas/database/peliculas.db"
        self.conexion=sqlite3.connect(self.db)

        #un cursor es un objeto que actúa como un intermediario o mensajero entre tu código y el motor de la base de datos.Si la conexión (connection) es el cable que une tu programa con el servidor, el cursor es la mano que envía las órdenes y recoge los resultados.Tiene 3 responsabilidades, ejecutar comandos sql,gestionar los resultados,osea el cursor no descarga todo de golpe necesariamente; te permite "navegar" por esos datos fila por fila o en grupos.Y mantiene la posicion, el cursor funciona como un "puntero". Sabe en qué fila de los resultados te encuentras actualmente para que, al pedir la siguiente, sepa exactamente cuál entregarte.
        self.cursor=self.conexion.cursor()

    def cerrarConexion(self):
        self.conexion.commit()
        self.conexion.close()