registroEstudiantes=[]

while True:
    print("1. Registrar estudiante")
    print("2. Mostrar registro")
    print("3. Salir")

    opcion= input("Seleccione una opción: ")

    if opcion=="1":
        #registrar estudiante
        nombre=input("Ingrese el nombre del estudiante: ")
        edad=int(input("Ingrese la edad del estudiante: "))
        curso=input("Ingrese el curso del estudiante: ")

        #creamos el diccionario que va almacenando cada dato del estudiante
        estudiante={"nombre":nombre,"edad":edad, "curso":curso}

        #almacenamos en la lista los diccionarios creados
        registroEstudiantes.append(estudiante)
        print("Estudiante registrado exitosamente!")

    elif opcion=="2":
        if registroEstudiantes:
            print("\nRegistro de estudiantes:")

            for estudiante in registroEstudiantes:
                print(f"nombre:{estudiante['nombre']},edad:{estudiante['edad']},curso:{estudiante['curso']} \n")
        
        else:
            print("El registro está vacio. Registr estudiantes primero")

    elif opcion=="3":
        print("Saliendo del programa. !Adios!")
        break
    else:
        print("opción no válida. Intente de nuevo")




