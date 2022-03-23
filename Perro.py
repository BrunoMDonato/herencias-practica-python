from Animal import Animal
from Mamiferos import Mamiferos


class Perro(Animal, Mamiferos):

    def __init__(self, cant_patas, nombre, raza, color):
        Animal.__init__(self, cant_patas, nombre)
        Mamiferos.__init__(self, raza)
        self.color = color



perrito = Perro(4, 'Lolo', 'Labrador', 'Marron')

print(perrito.moverse())
print(perrito.color)
print(perrito.cant_patas)
print(perrito.nombre)
print(perrito.raza)
print(perrito.mamar())
