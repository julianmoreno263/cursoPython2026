#trabajando con modulos en python, hay modulos propios del lenguaje,de terceros o los que nosotros creamos, un modulo es un archivo de python con codigo,un paquete es una carpeta con varios modulos que se relacionan,por ejemplo en una aaplicacion exha en python,la podemos dividir en paquetes,uno con los archivos del frontend,otro con los modulos de la conexion al backend,etc. Para ver los modulos propios del lenguaje vamos a la documentacion,veremos algunos aqui.


#al importar un modulo podemos ponerle un alias con as
# import datetime as dt

#si solo quiero importar clases especificas de un modulo utilizo la palabra from,tambien le podemos poner alias,pero es mejor poner el nombre del modulo para ser mas claros
# from datetime import date as d
# from datetime import datetime as dt

#si queremos utilizar todo lo de un modulo utilizamos el * , pero no es buena practica porque si no necesitamos todo lo de ese modulo lo que estamos haciendo es hacer mas pesado el programa,toca saber utilizarlo.

# from datetime import date,datetime
import os
import time
from mi_paquete import modulo1 #aqui estamos importando el modulo del paquete mi_paquete
from colorama import init,Fore# paquete para colorear la consola

# hoy=date.today()
# ahora=datetime.now()

# print(hoy)
# print(ahora)

# modulo1.saludar()

#la variable global __name__ nos indica el nombre del archivo que estamos ejecutando,por ejemplo si imprimimos esta variable aqui en este archivo nos indicara el nombre __main__ que es el nombre del archivo donde estamos ejecutando codigo,si ponemos esta variable por ejemplo en un modulo nos indicara la ruta de ese modulo. En si __name__ se utiliza para indicar cual es el archivo principal desde donde se ejecutara el programa en python,esto se hace con un condicional if asi:
# if __name__=="__main__":
#     print("Este es el archivo principal del programa")
#     modulo1.saludar()

# print(__name__)

init()#asi inicializamos colorama
if __name__=="__main__":
    print(Fore.RED + ("Mensaje de alerta en rojo"))
    print(Fore.GREEN + ("Mensaje de alerta en verde"))
    print(Fore.BLUE + ("Mensaje de alerta en azul"))


#ahora, el manejador de paquetes de python se llama pip,con pip podemos instalar paquetes externos que necesitemos usar. Para usar pip debo poner: python -m pip y el paquete,La bandera -m significa "module-name". Esto le dice a Python: "Busca en tu configuración interna el módulo llamado pip y ejecútalo". 


#con esto puedo limpiar la terminal despues de 3 segundos automaticamente
time.sleep(3)
os.system("cls")



