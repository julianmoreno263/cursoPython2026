#modulo en un paquete

#el archivo __init__.py dentro del paquete indica que esa carpeta es un paquete

from mi_paquete import variableGolbal

def saludar():
    print("Hola desde el modulo 1")

print(variableGolbal)