import tkinter as tk
from client.gui_app import Frame, barraMenu

def main():
    root=tk.Tk()
    root.title("Catálogo Películas")
    root.iconbitmap("catalogo_peliculas/img/cp-logo.ico")
    root.resizable(False,False)
    barraMenu(root)

    #instanciamos el frame
    app=Frame(root=root)
    

    app.mainloop()


if __name__ =="__main__":
    main()