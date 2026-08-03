
from django.http import HttpResponse

#creamos nuestra primera vista, la request en si es la ruta que se llama desde el archivo url.py,osea la ruta 'hola/' es la peticion del cliente,esta peticion es la request que se pasa aqui como parametro y ejecuta la funcion.
def hola(request):
    return HttpResponse('Hola mundo de Django')


def verificar(request,nombre,edad):
    if edad<12:
        mensaje=f'Hola {nombre}, no puedes entrar!'
    else:
        mensaje=f'Hola {nombre}, puedes ingresar!'

    return HttpResponse(mensaje)