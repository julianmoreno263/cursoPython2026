import sqlite3
import os
import sys

#funcion para que al crear el ejecutable no cree una base de datos temporal sino que utilice la de sqlite3 y los datos persistan
def obtener_ruta_db(nombre_relativo):
    if getattr(sys, 'frozen', False):
        # MODO EJECUTABLE: sys.executable apunta a la carpeta del .exe
        base_path = os.path.dirname(sys.executable)
    else:
        # MODO DESARROLLO (VS Code): 
        # __file__ es: .../catalogo_peliculas/model/conexionDB.py
        # Usamos dirname dos veces para subir de 'model' a la raíz 'catalogo_peliculas'
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    return os.path.join(base_path, nombre_relativo)

#clase para conectar la bd
class ConexionDB:
    #el constructor crea el archivo peliculas.db si no existe
    def __init__(self):
        # Esto buscará la carpeta 'database' en la raíz del proyecto
        self.ruta_db = obtener_ruta_db(os.path.join("database", "peliculas.db"))

          #un cursor es un objeto que actúa como un intermediario o mensajero entre tu código y el motor de la base de datos.Si la conexión (connection) es el cable que une tu programa con el servidor, el cursor es la mano que envía las órdenes y recoge los resultados.Tiene 3 responsabilidades, ejecutar comandos sql,gestionar los resultados,osea el cursor no descarga todo de golpe necesariamente; te permite "navegar" por esos datos fila por fila o en grupos.Y mantiene la posicion, el cursor funciona como un "puntero". Sabe en qué fila de los resultados te encuentras actualmente para que, al pedir la siguiente, sepa exactamente cuál entregarte.
        # self.cursor=self.conexion.cursor()
        
        try:
            # Conexión normal
            self.conexion = sqlite3.connect(self.ruta_db)
            self.cursor = self.conexion.cursor()
        except sqlite3.OperationalError as e:
            print(f"Error: No se pudo abrir la base de datos en {self.ruta_db}")
            print(f"Detalle del error: {e}")


            
    # def __init__(self) -> None:
    #     # self.db=r"6-proyecto/catalogoPeliculas/catalogo_peliculas/database/peliculas.db"
    #     # self.conexion=sqlite3.connect(self.db)

    #     # Esto obtiene la ruta de la carpeta donde está este archivo .py
    #     ruta_base = os.path.dirname(__file__)
    #     #Sube un nivel a 'catalogo_peliculas'
    #     ruta_proyecto = os.path.dirname(ruta_base)
    #     # Esto apunta a la base de datos dentro de esa misma carpeta
    #     self.db = os.path.join(ruta_proyecto, 'database', 'peliculas.db')
        
    #     try:
    #         self.conexion = sqlite3.connect(self.db)
    #         self.cursor = self.conexion.cursor()
    #     except sqlite3.OperationalError:
    #         print("Error: No se pudo abrir la base de datos. Verifica la ruta.")

      

    def cerrarConexion(self):
        self.conexion.commit()
        self.conexion.close()