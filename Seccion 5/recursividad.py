#Ejercicios de recursividad

def recursion(i):
    if(i < 1):
        return i
    print(i)
    recursion(i-1)

recursion(10)

#La recursividad nos sirve para cuando querramos reintentar hacer
#varios intentos de iteracion de una coleccion o intentar conectarnos
# a un servidor para poder volver a tratar de hacer una conexion.
# Otro caso es para hacer procesamientos en batch, una lista con 50 elementos por ejemplo.
