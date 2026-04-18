from mascotas2 import Mascota,RegistroMascotas

registro=RegistroMascotas()

while True:
    menu="""---MENU---
    1. Agregar mascota
    2. Listar mascota
    3. Editar mascota
    4.Eliminar mascota
    5. Salir
    Ingrese una opción: """

    opcion=input(menu)

    if opcion=="1":
        nombre=input("Nombre de la mascota: ")
        especie=input("Especie de la mascota: ")
        edad=input("Edad de la mascota: ")

        mascota=Mascota(especie,edad,nombre)
        registro.agregarMascota(mascota)
    
    elif opcion=="2":
        registro.listarMascotas()
    
    elif opcion=="3":
        indice=int(input("Ingrese el índice del registro: "))
        nombre=input("Nombre de la mascota: ")
        especie=input("Especie de la mascota: ")
        edad=input("Edad de la mascota: ")

        nuevaMascota=Mascota(especie,edad,nombre)
        registro.editarMascota(indice-1,nuevaMascota)

    elif opcion=="4":
        indice=int(input("Ingrese el índice del registro a eliminar: "))
        registro.eliminarMascota(indice-1)
    
    elif opcion=="5":
        print("Hasta luego!!")
        break

    else:
        print("Opción inválida. Por favor elija una opción válida")


