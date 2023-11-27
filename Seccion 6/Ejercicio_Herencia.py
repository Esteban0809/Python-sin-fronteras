#Ejercicio de Herencial

class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print("Hola soy un ",self.tipo ," y mi sonido es el", self.onomatopeya)

class Gato(Animal):
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya): # <- Al poner un __init__ dentro de la clase hija deshabilitamos el init del padre
        Animal.__init__(self, nombre, onomatopeya) # <- a menos que mandemos llamar al init del padre enviandole los datos includio el self
        print('Hola soy un gato extendido') # <- Para poder extender su comportamiento segun necesitemos

gato = Gato('Fluffy', 'Maullido')
gato.saludo()

class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre,onomatopeya) # <- super siempre hace referencia a la clase padre, y para extenderlo debemos ejecutar el de la clase padre
        print('Instanciando un perro')
class Canario(Animal):
    tipo = 'canario'

perro = Perro('Firulais', 'Ladrido')
perro.saludo()

canario = Canario('Piolin', 'Silvido')
canario.saludo()