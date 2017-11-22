class Persona():
    def __init__(self,nombre):
        self.nombre = nombre

    def camina(self):
        print('caminando')
    def duerme(self):
        print('durmiendo')
    def come(self):
        print('comiendo')

class Hijo(Persona):
    def camina(self):
        print('Camina rapido')
