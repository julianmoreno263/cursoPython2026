
from gc import disable
import tkinter as tk
from turtle import width


#clase para el Frame
class Frame(tk.Frame):
    def __init__(self, root=None) -> None:
        super().__init__(root,width=480,height=320)
        self.root=root
        self.pack()
        # self.config(bg="green")

        self.camposPelicula()

    def camposPelicula(self):
        #labels de cada campo
        self.labelNombre=tk.Label(self,text="Nombre: ")
        self.labelNombre.config(font=("Arial",12,"bold"))
        self.labelNombre.grid(row=0,column=0,padx=10,pady=10)

        self.labelDuracion=tk.Label(self,text="Duración: ")
        self.labelDuracion.config(font=("Arial",12,"bold"))
        self.labelDuracion.grid(row=1,column=0,padx=10,pady=10)

        self.labelGenero=tk.Label(self,text="Género: ")
        self.labelGenero.config(font=("Arial",12,"bold"))
        self.labelGenero.grid(row=2,column=0,padx=10,pady=10)

        #entryes de cada campo
        self.entryNombre=tk.Entry(self)
        self.entryNombre.config(width=50,state="disabled",font=("Arial",12))
        self.entryNombre.grid(row=0,column=1,padx=10,pady=10)

        self.entryDuracion=tk.Entry(self)
        self.entryDuracion.config(width=50,state="disabled",font=("Arial",12))
        self.entryDuracion.grid(row=1,column=1,padx=10,pady=10)

        self.entryGenero=tk.Entry(self)
        self.entryGenero.config(width=50,state="disabled",font=("Arial",12))
        self.entryGenero.grid(row=2,column=1,padx=10,pady=10)



#funcion para el menu
def barraMenu(root):
    barraMenu=tk.Menu(root)
    root.config(menu=barraMenu, width=300, height=300)

    #pestañas del menu con sus respectivos submenus
    menuInicio=tk.Menu(barraMenu,tearoff=0)
    barraMenu.add_cascade(label="Inicio",menu=menuInicio)
    menuInicio.add_command(label="Crear Registro en DB")
    menuInicio.add_command(label="Eliminar Registro en DB")
    menuInicio.add_command(label="Salir", command=root.destroy)

   
    barraMenu.add_cascade(label="Consultas")
    barraMenu.add_cascade(label="Configuración")
    barraMenu.add_cascade(label="Ayuda")

    
   
