

#clase para representar un animal
class Animal:
    def __init__(self,especie,edad) -> None:
        self.especie=especie #atributo publico en python
        self.edad=edad
    
    def __str__(self) -> str:
        return f"Animal [Especie: {self.especie}, Edad: {self.edad}]"



#esta clase es para representar una mascota,hereda de la clase Animal
class Mascota(Animal):
    def __init__(self, especie, edad,nombre) -> None:
        super().__init__(especie, edad)
        self.nombre=nombre#atributo privado en python

    def __str__(self) -> str:
        return f"Mascota [Nombre: {self.nombre},Especie: {self.especie}, Edad: {self.edad}]"

 
#clase para el registro de las mascotas
class RegistroMascotas:
    def __init__(self):
        self.mascotas=[]

    #agrega una mascota al array de mascotas
    def agregarMascota(self,mascota):
        self.mascotas.append(mascota)

    #lista las mascotas
    def listarMascotas(self):
        if self.mascotas:
            print(" Lista de mascotas \n","="*30)

            for i, mascota in enumerate(self.mascotas, start=1):
                print(f"{i}. {mascota}")
        
        else:
            print("No hay mascotas registradas")

    
    #edita una mascota, el parametro nuevaMascota sera la nueva informacion de la mascota
    def editarMascota(self,indice,nuevaMascota):
        if indice<0 or indice>=len(self.mascotas):
            print("No hay registro con ese índice")
        else:
            self.mascotas[indice]=nuevaMascota
            print("Mascota editada correctamente")



    #elimina una mascota por su indice
    def eliminarMascota(self,indice):
        if indice<0 or indice>=len(self.mascotas):
            print("No hay registro con ese índice")
        else:
            del self.mascotas[indice]
            print("Mascota eliminada correctamente")