import random

print("Bienvenido al juego!!. Adivina el número")

numSecreto=random.randint(1,100)
intentosMax=10
intentosRealizados=0

while intentosRealizados < intentosMax:
    intento=int(input("Adivina el numero entre 1 y 100: "))
    intentosRealizados+=1

    if intento==numSecreto:
        print(f"Felicidades, adivinaste el número en {intentosRealizados} intentos")
        break
    elif intento < numSecreto:
        print(f"El número debe ser mayor.\n Te quedan {intentosMax-intentosRealizados} intentos")
    else:
        print(f"El número debe ser menor.\n Te quedan {intentosMax-intentosRealizados} intentos")

if intentosRealizados==intentosMax:
    print("GAME OVER")
 