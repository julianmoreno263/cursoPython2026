
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from model.peliculaCrud import crearTabla,borrarTabla
from model.peliculaCrud import Pelicula, guardarPelicula,listarPelicula,editarPelicula


#clase para el Frame
class Frame(tk.Frame):
    def __init__(self, root=None) -> None:
        super().__init__(root,width=480,height=320)
        self.root=root
        self.pack()
        # self.config(bg="green")

        self.idPelicula=None

        self.camposPelicula()
        self.deshabilitarCampos()
        self.tablaPeliculas()

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
        self.miNombre=tk.StringVar()
        self.entryNombre=tk.Entry(self,textvariable=self.miNombre)
        self.entryNombre.config(width=50,font=("Arial",12))
        self.entryNombre.grid(row=0,column=1,padx=10,pady=10,columnspan=2)

        self.miDuracion=tk.StringVar()
        self.entryDuracion=tk.Entry(self,textvariable=self.miDuracion)
        self.entryDuracion.config(width=50,font=("Arial",12))
        self.entryDuracion.grid(row=1,column=1,padx=10,pady=10,columnspan=2)

        self.miGenero=tk.StringVar()
        self.entryGenero=tk.Entry(self,textvariable=self.miGenero)
        self.entryGenero.config(width=50,font=("Arial",12))
        self.entryGenero.grid(row=2,column=1,padx=10,pady=10,columnspan=2)

        #Botones
        self.botonNuevo=tk.Button(self,text="Nuevo", command=self.habilitarCampos)
        self.botonNuevo.config(width=20,font=("Arial",12,"bold"),fg="#DAD5D6",bg="#158645"
                               ,cursor="hand2",activebackground="#35BD6F")
        self.botonNuevo.grid(row=3,column=0,padx=10,pady=10)

        self.botonGuardar=tk.Button(self,text="Guardar", command=self.guardarDatos)
        self.botonGuardar.config(width=20,font=("Arial",12,"bold"),fg="#DAD5D6",bg="#1658A2"
                               ,cursor="hand2",activebackground="#3586DF")
        self.botonGuardar.grid(row=3,column=1,padx=10,pady=10)

        self.botonCancelar=tk.Button(self,text="Cancelar",command=self.deshabilitarCampos)
        self.botonCancelar.config(width=20,font=("Arial",12,"bold"),fg="#DAD5D6",bg="#BD152E"
                               ,cursor="hand2",activebackground="#E15370")
        self.botonCancelar.grid(row=3,column=2,padx=10,pady=10)

    #metodos para habilitar entryes
    def habilitarCampos(self):
        self.entryNombre.config(state="normal")
        self.entryDuracion.config(state="normal")
        self.entryGenero.config(state="normal")

        self.botonGuardar.config(state="normal")
        self.botonCancelar.config(state="normal")

    def deshabilitarCampos(self):
        #enviamos datos vacios al momento de deshabilitar los entryes para que se borren los datos que puedan tener
        self.miNombre.set("")
        self.miDuracion.set("")
        self.miGenero.set("")

        self.entryNombre.config(state="disabled")
        self.entryDuracion.config(state="disabled")
        self.entryGenero.config(state="disabled")

        self.botonGuardar.config(state="disabled")
        self.botonCancelar.config(state="disabled")
            

    def guardarDatos(self):
        #asi capturamos lo que hay en los entry para guardarlos en la bd
        pelicula=Pelicula(
            self.miNombre.get(),
            self.miDuracion.get(),
            self.miGenero.get()
        )

        #condicional para guardar o editar pelicula
        if self.idPelicula==None:
            guardarPelicula(pelicula)
        else:
            editarPelicula(pelicula,self.idPelicula)


        self.tablaPeliculas()#con esta linea vamos actualizando la lista de peliculas en la GUI
        self.deshabilitarCampos()

    #funcion para crear la tabla de la bd
    def tablaPeliculas(self):

        #aqui recuperamos la lista de peliculas
        self.listaPeliculas=listarPelicula()
        self.listaPeliculas.reverse()#invertimos la lista porque al mostrarla la esta mostrando invertida



        self.tabla=ttk.Treeview(self,columns=("Nombre","Duración","Género"))                       
        self.tabla.grid(row=4,column=0,columnspan=4,sticky="nse")

        #scroll bar para la tabla si excede 10 registros
        self.scroll=ttk.Scrollbar(self, orient="vertical",command=self.tabla.yview)
        self.scroll.grid(row=4,column=4,sticky="nse")
        self.tabla.configure(yscrollcommand=self.scroll.set)

        #creamos los encabezados
        self.tabla.heading("#0",text="ID")
        self.tabla.heading("#1",text="NOMBRE")
        self.tabla.heading("#2",text="DURACIÓN")
        self.tabla.heading("#3",text="GÉNERO")

        #iteramos la lista de peliculas
        for p in self.listaPeliculas:
            self.tabla.insert("",0,text=p[0],values=(p[1],p[2],p[3]))

        #boton de editar
        self.botonEditar=tk.Button(self,text="Editar",command=self.editarDatos)
        self.botonEditar.config(width=20,font=("Arial",12,"bold"),fg="#DAD5D6",bg="#158645"
                               ,cursor="hand2",activebackground="#35BD6F")
        self.botonEditar.grid(row=5,column=0,padx=10,pady=10)

        #boton eliminar
        self.botonEliminar=tk.Button(self,text="Eliminar")
        self.botonEliminar.config(width=20,font=("Arial",12,"bold"),fg="#DAD5D6",bg="#BD152E"
                               ,cursor="hand2",activebackground="#E15370")
        self.botonEliminar.grid(row=5,column=1,padx=10,pady=10)

    def editarDatos(self):
        try:
            # 1. Obtenemos la tupla de selección
            seleccion = self.tabla.selection()
        
            # 2. Si hay algo seleccionado, extraemos el ID
            if seleccion:
                # Agregamos [0] para sacar el primer elemento de la tupla, asi recuperamos los datos de la tabla GUI
                self.idPelicula = self.tabla.item(seleccion[0])["text"]
                self.nombrePelicula=self.tabla.item(seleccion[0])["values"][0]
                self.duracionPelicula=self.tabla.item(seleccion[0])["values"][0]
                self.generoPelicula=self.tabla.item(seleccion[0])["values"][0]

                #luego de capturar los datos,habilitamos los entryes
                self.habilitarCampos()
                #los datos que capturamos los escribimos en los entryes para poder editarlos
                self.entryNombre.insert(0,self.nombrePelicula)
                self.entryDuracion.insert(0,self.duracionPelicula)
                self.entryGenero.insert(0,self.generoPelicula)

        except:
            titulo="Edición de datos"
            mensaje="No ha seleccionado ningun registro"
            messagebox.showerror(titulo,mensaje)



#funcion para el menu
def barraMenu(root):
    barraMenu=tk.Menu(root)
    root.config(menu=barraMenu, width=300, height=300)

    #pestañas del menu con sus respectivos submenus
    menuInicio=tk.Menu(barraMenu,tearoff=0)
    barraMenu.add_cascade(label="Inicio",menu=menuInicio)
    menuInicio.add_command(label="Crear Registro en DB",command=crearTabla)
    menuInicio.add_command(label="Eliminar Registro en DB",command=borrarTabla)
    menuInicio.add_command(label="Salir", command=root.destroy)

   
    barraMenu.add_cascade(label="Consultas")
    barraMenu.add_cascade(label="Configuración")
    barraMenu.add_cascade(label="Ayuda")

    
   
