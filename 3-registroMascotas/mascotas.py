#POO en python


#clase para representar un animal
class Animal:
    def __init__(self,especie,edad) -> None:
        self.especie=especie #atributo publico en python
        self.edad=edad
    
    #En Python, los métodos que empiezan y terminan con doble guion bajo (llamados dunder methods) tienen funciones especiales. __str__ se encarga de devolver una representación en texto (una cadena o string) que sea fácil de leer para los humanos.
    def __str__(self) -> str:
        return f"Animal [Especie: {self.especie}, Edad: {self.edad}]"



#herencia
class Mascota(Animal):
    #esta clase es para representar una mascota,hereda d ela clase Animal
    def __init__(self, especie, edad,nombre) -> None:
        super().__init__(especie, edad)
        self.__nombre=nombre#atributo privado en python

    def info(self):
        print(f"Nombre: {self.__nombre}, Especie: {self.especie}, Edad: {self.edad}")

    def hablar(self):
        pass

    #metodo getter para obtener el atributo privado __nombre
    def getNombre(self):
        return self.__nombre
    
    #metodo setter para modificar el atributo privado nombre
    def setNombre(self,nombre):
        self.__nombre=nombre



#polimorfismo,hacer que los metodos heredados desde una clase se comporten de forma diferente en los objetos creados de otras clases(hijas)
class Perro(Mascota):
    def hablar(self):
        return "Woof!"

    
class Gato(Mascota):
    def hablar(self):
        return "Miau!"

p=Perro("Perro",2,"Firulais")
g=Gato("Gato",2,"Pelusa")

print(p.hablar())
print(g.hablar())


#encapsulacion, permite ocultar los detalles de la implementacion de una clase,por ejemplo podemos ocultar nuestros atributos usando modificadores de acceso, en otros lenguajes son palabras reservadas que le dan la caracteristica de publico o reservado a los atributos, en python no existen esas palabras, en cambio se ponen dos barras bajas baja "__". y asi el atributo sera privado,no podemos acceder directamente al atributo, por ejemplo el atributo nombre de la clase Mascota es privado, si intentamos modificarlo directamente no se puede,osea modificarlo fuera de la clase. Para poder modificarlo debemos crear dentro de la clase metodos setter y getter que nos permitan modificar esos atributos privados.

#estos atributos privados se necesitan cuando no queremos que se puedan manipular los atributos por fuera de la clase.

mascota1=Mascota("perro","6 meses","boby")
mascota1.edad=4

mascota1.setNombre("firulais")
mascota1.info()
print(mascota1.getNombre())



