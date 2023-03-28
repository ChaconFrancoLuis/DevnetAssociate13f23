# variables de instancia y variables de clase
"""class carro:
    Fabricante = "Toyota"

    def __init__(self, modelo, year):
        self.marca = modelo
        self.year = year

    def movimiento(self):
        print("el automovil se esta moviendo")

carro1 = carro("Rav4","1999")
carro1.movimiento()"""
#=============================================================
"""
class ubicacion:
    Continente = "America"
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def Miubicacion(self):
        print("Hi, my name is " + self.name + " and I live in " +self.country + ".")

#Instancia de objetos loc, loc1, loc2 de la clase ubicacion()
loc = ubicacion("Luis", "Guatemala")
loc1 = ubicacion("Carlos","Colombia")
loc2 = ubicacion("Jessy","Puerto Rico")

# uso de metodo miubicacion()
loc.Miubicacion()
loc1.Miubicacion()
loc2.Miubicacion()"""
#=============================================================
# Encapsulacion
"""class coche:
    def __init__(self,marca,modelo):
        self.__marca = marca
        self.__modelo = modelo

    def obtener_informacion(self):
        return f"{self.__marca}{self.__modelo}"


carro1 = coche("toyota","2000")

print(carro1.obtener_informacion())"""
#=============================================================
# Abstraccion de datos
"""
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio * self.radio

circulo = Circulo(3)
print(circulo.area())"""

#=============================================================
# Polimorfismo - objeto y su habilidad para tomar multiples formas
"""
class Animal:
    def sonido(self):
        return "Algún sonido"

class Perro(Animal):
    def sonido(self):
        return "Guau!"

class Gato(Animal):
    def sonido(self):
        return "Miau!"

def hacer_sonido(animal):
    print(animal.sonido())

#creacion de objetos de diferentes clases
animal = Animal()
perro = Perro()
gato = Gato()

hacer_sonido(animal)  # Salida: Algún sonido
hacer_sonido(perro)   # Salida: Guau!
hacer_sonido(gato)    # Salida: Miau!"""


#=============================================================
# Herencia - clase hija obtiene propiedades de clase padre
"""
class Vehiculo:
    def mover(self):
        return "El vehiculo se mueve"

class Coche(Vehiculo):
    def mover(self):
        return "el coche esta conduciendo"

coche = Coche()
print(coche.mover())"""

#=============================================================
# Ejemplo - clase Estudiante

"""
class Estudiante:
    total_estudiantes = 0

    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Estudiante.total_estudiantes += 1
    
    def printEstudiante(self):
        print(f"Estudiante 1:{estudiante1.nombre}, Edad:{estudiante1.edad}")

#crear objetos de la clase estudiante
estudiante1 = Estudiante("Carlos",22)
estudiante2 = Estudiante("Ana",25)
estudiante3 = Estudiante("Luis",28)
estudiante4 = Estudiante("Yenny",30)

estudiante1.printEstudiante()

print(f"Total de estudiantes:{Estudiante.total_estudiantes}")
"""

