# mi_dic={}
# print(type(mi_dic))

datosPersonales={"nombre":"juan", "edad":30, "ciudad":"lima" }
print(datosPersonales["nombre"])

#para saber si una clave existe en el diccionario
print("edad" in datosPersonales)

#agregar otro elemento, si la clave existe podemos modificar el valor
datosPersonales["clave1"]="valor1"
print(datosPersonales)

#tambien sirve update()
datosPersonales.update({"clave2":"valor2"})
print(datosPersonales)

#con del pasando la clave borro el elemento
del datosPersonales["clave1"]
print(datosPersonales)


print(len(datosPersonales))

#para obtener las claves o las listas
print(datosPersonales.keys())
print(datosPersonales.values())

#iterar diccionario
for clave,valor in datosPersonales.items():
    print(f"{clave}: {valor}")
