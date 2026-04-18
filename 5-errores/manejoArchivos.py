
try:
    #abrir archivos en modo lectura, con with abre el archivo y lo cierra de forma automatica,es mas limpio,por lo que no necesitariamos usar el finally con el close()
    with open("archivo.txt","r") as archivo:
       #leer el contenido del archivo
        contenido=archivo.read()
except FileNotFoundError:
    print("El archivo no se ha encontrado")
    print("Creando el archivo...")
    with open("archivo.txt","w") as archivo:#cuando abrimos un archivo en modo w,si no existe open lo crea
        archivo.write("Hola mundo")
else:
    print("Contenido del archivo")
    print(contenido)
# finally:
#     if archivo:
#         archivo.close()