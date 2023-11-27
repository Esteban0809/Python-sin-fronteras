# Escribir una funcion que nos indique  si un numero es par o impar
numero = int(input('Ingresa un numero para verificar si es par: '))

def esPar(numero):
    return numero % 2 == 0

resultado = esPar(numero)
print(resultado)