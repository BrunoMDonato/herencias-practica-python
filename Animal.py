
#clase padre
class Animal:

    def __init__(self, cant_patas, nombre):
        self.cant_patas = cant_patas
        self.nombre = nombre

    def moverse(self):
        return f'Me estoy moviendo sobre mis {self.cant_patas} patas'

    def dormir (self):
        return 'Estoy durmiendo'