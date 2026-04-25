import tkinter as tk
from client.gui_app import Frame, barraMenu

import os
import sys


#funcion para capturar bien las rutas de los archivos externos como img y database para que al crear el ejecutable no haya errores y se pueda ejecutar de ambas formas,tanto de vscode con su terminal como desde el ejecutable que se crea.
def recurso_ruta(relative_path):
    """ Obtiene la ruta absoluta de los recursos, funciona para dev y para PyInstaller """
    try:
        # Si PyInstaller empaquetó el archivo, sys._MEIPASS existe
        base_path = sys._MEIPASS # type: ignore
    except AttributeError:
        # Si estamos en VS Code, usamos la ubicación real del archivo .py
        # Esto garantiza que encuentre la carpeta 'img' aunque abras la terminal en otro sitio
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_path, relative_path)

def main():
    root=tk.Tk()
    root.title("Catálogo Películas")
    #asi se pone la ruta del .ico para crear el ejecutable
    ruta_icono = recurso_ruta(os.path.join("img", "cp-logo.ico"))
    root.iconbitmap(ruta_icono)
    root.resizable(False,False)
    barraMenu(root)

    #instanciamos el frame
    app=Frame(root=root)
    

    app.mainloop()


if __name__ =="__main__":
    main()