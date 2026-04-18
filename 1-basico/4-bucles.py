#while
# contador=1

# while contador<=10:
#     print(contador)
#     contador+=1


#lista de productos
listaProductos=[]
producto=""


#el while me sirve para hacer que algo se repita muchas veces, como en este caso la instruccion input
while producto.lower() !="salir":
    producto=input("Ingrese un producto,(escriba salir para terminar): ")
    if producto=="salir":
        break
    else:
        listaProductos.append(producto)

print("\nLista de productos")

#iteramos la lista con while
# contador=1
# indice=0

# while indice < len(listaProductos):
#     print(f" {contador}. {listaProductos[indice]}")
#     indice+=1
#     contador+=1

#iteramos la lista con for, el for es para iterar sobre listas, es mas facil
for i in listaProductos:
    print(i)


