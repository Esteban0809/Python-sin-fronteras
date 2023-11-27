# Funciones
# Se usan para reautilziar codigo, no se ejecutan a menos que se
# las llame

# def nos ayudara para definir funciones
def  miFuncion():
    print('Mi primera funcion')

#miFuncion()

# pueden recibir argumentos, los cuales podamos usar dentro de ellas
# para que sean flexibles para tener diferentes comportamientos para
# en funcion a los argumentos para
def imprimeDato(argumento1, argumento2):
    print('el argumento es', argumento1, ' y es del tipo ', argumento2)

#imprimeDato('Chanchito feliz','Volador')

#Se le deben proporcionar la cantidad de argumentos, de lo contrario nos dara error.
#Se puede acceder a elementos variables con la siguiente sintaxis
# El simbolo * indica que los argumentos pueden ser variables
# Enviar el arg sin especificar con [] imprimiria todos los argumentos en una tupla
def imprimeDato2(*nombre):
    print('El dato enviado es: ', nombre[1])

#imprimeDato2('chanchito','feliz')

#Si no recordamos el orden de los argumentos podemos especificarlos directamentes
def nombreCompleto(apellido,nombre):
    print(nombre,apellido)

#nombreCompleto(nombre='Chanchito', apellido='Feliz')

#Tambien podemos acceder a ellas con las siguientes sintaxis **kwargs
# o tambien conocido como keywoard args

def nombreCompleto2(**kwargs):
    print(kwargs['nombre'],kwargs['apellido'])

#nombreCompleto2(nombre='Chanchito',apellido='Feliz')


#Podemos asignar valores por defecto en caso que no se proporcione ninguno

def miFuncion2(argumento = 'Chanchito'):
    print(argumento)

#miFuncion2('Batman')
#miFuncion2()

def miFuncionLista(lista):
    for el in lista:
        print(el)

#miFuncionLista(['Chanchito','Feliz'])

def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + ' ' + el
    return i

nombres = concatenaNombres(['Chanchito','Feliz'])
print(nombres)