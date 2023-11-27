# Ingresar nombre y apellido e imprimirlo al revez

nombre = input('Ingresa tu nombre amiguito: ')
apellido = input('Ingresa ahora tu apellido: ')

def reverso_nombres(nombre,apellido):
   concatenacion = nombre + ' ' + apellido
   print(concatenacion[::-1])

reverso_nombres(nombre,apellido)