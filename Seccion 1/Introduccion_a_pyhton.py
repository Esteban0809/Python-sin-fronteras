
#REPL de python
# Por REPL se refiere a el modo de el cmd al insertar el comando de python.
# REPLS siginfica (Read, Evaluate, Print y Loop)

#La identacion del codigo es primordial en python, de no estar identado el print con un tab no estaria dentro 
# del if

if 5 > 3:
    print("5 es mayor a 3") # Esta condicion se cumple

if 3 > 5:
    print("Esto no se va a imprimir porque no se cumple la condicion") #Esta condicion no se ejecuta

# COMENTARIOS
# Los comentarios se agregan con el simbolo del #
# Son buenos para guiarnos dentro del codigo si lo retomamos despues o para otros desarrolladores
# Pero no hay que abusar de ellos

# VARIABLES

x = 5
y = 'Hellow World'
print(x,y)

email = 'hellowWorld@mail.com'
print(email)

mivar = 'chanchito'
#mi_var= 'chanchito2'
#_mi_var = 'chanchito3'
#miVar = 'chanchito4'
#MIVAR = 'chanchito5'
#No podemos crear variables que comienzen en numero, tiene que ser despues de minimo una letra
# Da Error ---> 32variable = 5
variable32 = 4

#Python nos permite poder definir multiples variables en una sola linea
a, b ,c = 'Lala','Lele','Lili'
print(a)
print(b)
print(c)

# para declarar variables multiples con el mismo valor
valor1 = valor2 = valor3  = 'chanchito feliz'
print(valor1)
print(valor2)
print(valor3)

#CONCATENACION

inicio ='Hola'
final = 'Mundo'
print(inicio,final) # Hola Mundo
print (inicio + final) #
