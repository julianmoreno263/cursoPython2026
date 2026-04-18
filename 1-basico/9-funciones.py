# def saludar(nombre):
#     return f"Hola {nombre}, desde python"



#llamada ala funcion
# saludo=saludar("pepe")
# print(saludo)



# #funcion que trabaja con argumentos indefinidos,osea esta echa para poder trabajar con varios argumentos  de cualquier tipo o sin argumentos,se usa *args, devuelve una tupla 
# def args_func(*args):
#     print(args)

# args_func("hola",45,True)

# #con **kwargs una funcion puede recibir argumentos indefinidos por medio de una clave, retorna un diccionario
# def kwargs_func(**kwargs):
#     print(kwargs)

# kwargs_func(nombre="pepe",a=100, bool=False)

#anotaciones de tipo, en una funcion especifican el tipo de dato que debe recibir,y -> indica lo que la funcion va a retornar, pero esto no cambia la ejecucion del programa,osea si le indicamos int y le pasamos string igual ejecuta,esto solo es para que sea mas entendible
def suma(a:int, b:int)->int:
    return a+b

print(suma(2,5))

