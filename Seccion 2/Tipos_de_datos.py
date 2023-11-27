#En esta seccion veremos el uso de datos disponible que tenemos y como usarlos

#Tipo de dato string
#Puede definirse con ' simple o " doble
palabra = 'Hola Mundo'
oracion = "Hola Mundo como estas"

entero = 20 # integer
flotante = 20.3 # un float
#para definir numeros complejos tenemos que usarlos
complejo = 1j

#LISTAS
#es una coleccion de datos en la lista

lista = [1,2,3]

#agregar mas datos a la lista en la ultima posicion
lista.append(4)
#print(lista)
#para limpiar la lista 
#lista.clear()

#Para generar nuestra propia lista
lista2 = lista.copy()
lista2.append(5)
#print(lista,lista2)

#contar elementos y cuantas veces se repite en una lista
#print(lista2.count(5))
#print(len(lista), len(lista2))

largoLista = len(lista)
largoLista2 = len(lista2)

#print(largoLista, largoLista2)
#Accediendo a los elementos de la lista
#Los elementos comienzan del elemento 0 
#print(lista[0])

#Eliminando elementos de una lista2
#Metodo POP - elimina el ultimo elemento de una lista
lista.pop()
#print(lista)
#Si queremos eliminar un elemento en particular elegiremos el elemento a eliminar
lista.remove(1)
#print(lista)

#Ordenamiento Reverse y sort
nuevaLista = ['Hola','Mundo',4]
#print(nuevaLista)
#nuevaLista.sort() #No permite el uso de string y int en una misma lista, tiene que ser mismo tipo de dato
nuevaLista.reverse() #Permite uso de string y int
#print(nuevaLista)

#Tuplas
#La diferencia de las listas es que las tuplas no pueden ser modificadas una vez creadas, tienes que copiarla en una nueva para poder agregar elementos o cambiarlas
tupla = ('hola','mundo','somos','tupla')
#print(tupla.index('mundo'))
#print(tupla[0])
# tupla.append('chanchito') no funciona ya que no cuenta con el atributo de append
# para convertir la tupla en una lista2
listaDeTupla = list(tupla)
listaDeTupla.append('chanchito')
#print(listaDeTupla)

#Range
#Nos permiten tener muchos elementos
#Nos sirve para trabajar con las iteraciones
rango = range(6)
#print(rango)

#Diccionarios
#Son parecidos a las listas, la diferiencia radica en que vamos a utilizar en lugar de indices numericos, usaremos strings para referirnos a los indices
diccionario = {
    "nombre":"Chanchito",
    "raza":"persa",
    "edad":5
}
#print(diccionario)
#print(diccionario['raza'])
#print(diccionario.get('nombre'))
diccionario['nombre']= 'Migala'
#print(diccionario)

#para agregar valores dentro del diccionario
diccionario['ronronea'] = 'si'
#print(diccionario)

#para eliminar un elemento del diccionario 
diccionario.pop('ronronea')
#print(diccionario)

#podemos usar popitem que eliminara el ultimo elemento agregado al diccionario 
diccionario['eliminar']= 'si'
#print(diccionario)
diccionario.popitem()
#print(diccionario)

#tambien podemos usar del
del diccionario['edad']
#print(diccionario)

#Se pueden generar copias de los diccionarios
copiaGatito = diccionario.copy()
#print(copiaGatito)
#podemos eliminar todos los elementos dentro de un diccionario
diccionario.clear()
#print(diccionario)
#otra manera de generar copias es utilizar el element
copia2Gatito = dict(copiaGatito)
#print(copia2Gatito)

#Diccionarios anidados y constructor dict
mamba={
    'nombre':"Black Mamba",
    'edad':2
}
fluffy = {
    'nombre':"fluffy",
    'edad':4
}
gatitos = {
    "Fluffy":fluffy,
    "Mamba": mamba
}
#print(gatitos)
#print(gatitos['Fluffy'])

#Otra opcion que tenemos es usar el constructor dict, se va a llamar como si fuera una funcion 
# pero le vamos a pasar valores para que nos devuelva un diccionario
perritos = dict(nombre="Juancho", edad=4)

#print(perritos)

#Booleanos

verdadero = True
falso = False
print(verdadero, falso)




