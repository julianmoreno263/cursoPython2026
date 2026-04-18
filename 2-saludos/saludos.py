
#este archivo es un modulo con dos funciones

import random

def formatosAleatorios()->str:
    """
    retorna un saludo aleatorio con un nombre poporcionado
    """
    formatos=[
        "Hola {}, bienvenido",
        "Es genial verte {}",
        "Saludos, encantado de conocerte {}"
    ]

    return random.choice(formatos)



def hola(nombre:str)->str:
    """
    genera un saludo personalizado utilizando un nombre como argumento
    """
    if nombre=="":
        return "Error. Nombre vacio"

    saludo=formatosAleatorios().format(nombre)
    return saludo


def holas(nombres:list)->dict:
    saludos={}

    for nombre in nombres:
        saludo=hola(nombre)
        saludos[nombre]=saludo#aqui le pasamos al diccionario saludos cada saludo en el cual la clave sera el nombre y el valor el saludo
    return saludos

nombres=["Pedro","Juan","Mario"]

print(holas(nombres))