# msg="mi texto "
# msg1="este texto esta en python"
# msg2=msg+msg1
# print(msg2)
# print("hola " * 4)


# texto="python"
# print(len(texto))
# print(texto[:2]) 

#metodos de string
# texto1="hola mundo"
# texto2="Hola, hola, hola mundo"

# print(texto1.title())
# print(texto1.upper())
# print(texto1.lower())
# print(texto1.capitalize())

# print(texto2.count("hola"))
# print(texto2.find("H"))
# print("mundo" in texto2)

#formatos de cadena, f string
# nombre="pepe"
# edad=24
# talla=1.45

# print(f"Hola, mi nombre es {nombre}, tengo {edad} años y mido {talla} mts")

#ejercicio palindromo
palabra=input("Ingrese una palabra: ")
palabra=palabra.lower()
palabra=palabra.replace(" ","")
palabraInvertida=palabra[::-1]

if palabra==palabraInvertida:
    print(f"La palabra {palabra} es un palíndromo")
else:
    print(f"La palabra {palabra} no es un palíndromo")




