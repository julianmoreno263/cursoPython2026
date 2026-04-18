#para lanzar una exception personalizada en python podemos utilizar la palabra raise

#podemos crear una excepcion propia creandola como una clase que hereda de la clase Exception
class ColorNoValidoError(Exception):
    def __init__(self, color) -> None:
        super().__init__(f"El color {color} no se encuentra en la lista")


#funcion
def colores(color):
    lista_colores=["azul","verde","rojo"]

    if color not in lista_colores:
        raise ColorNoValidoError(color)
    

#llamado de la funcion con try-except
try:
    colores("morado")
except ColorNoValidoError as error:
    print(f"Error: {error}")