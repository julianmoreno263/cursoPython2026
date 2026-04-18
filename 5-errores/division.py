#vamos a ver como se manejan los errores en python, en si hay dos clases de errores en programacion, los errores de sintaxis y los de logica,para manejar los errores de logica usamos la estructura try-except. En el bloque de try se pone el codigo donde puede darse un error, y en el except se captura el error si lo hay, si no se sabe que tipo de error es se usa la clase Exception.Podemos poner varios except segun los errores que esperamos manejar. Lo que logramos con try-except es manejar los posibles errores,y asi haya un error el programa lo marca pero sigue ejecutando lo demas,no lo bloquea. Despues del except se puede poner un else que se ejecuta si no se ejecuta ninguna excepcion.

try:
    a=int(input("Ingrese el número entero: "))
    b=int(input("Ingrese un número entero diferente de cero: "))

    resultado=a/b
except ValueError:
    print("Error, debes ingresar números enteros")
except ZeroDivisionError:
    print("Error, nose puede dividir entre cero")
except Exception as e:
    print("Error",e)
else:
    print(f"División entre {a}/{b}: {resultado}")

print("Despues de excepciones sigue el programa")


