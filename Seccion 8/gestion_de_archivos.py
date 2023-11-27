import os

# La gestion de archivos es importante en el desarrollo webservices
# python afortunadamente nos da una herramienta que podemos usar para ello
here = os.path.dirname(os.path.abspath(__file__))
c = open(here+'\\'+'file.txt', 'w')
# el segundo argumento son permisos
# r para leer indicandolo desde el open 
# a para append y poder agregar contenido al final
# x para en caso de que nuestro archivo no exista lo va a crear, pero si existiera nos devolveria un error
# w es utilizado para escribir, pero es diferente su comportamiento al de usar c.write ya que eliminara todo el contenido anterior del archivo
# tambien podemos leer de una linea en una 
#print(c.readline())

# como no es conveniente leer linea por linea podemos usar un forma
#for x in c:
#    print(x)

# read es un metodo que tendra nuestro objeto c, que nos devolvera todo el archivo, no linea por linea
#print(c.read())

#siempre que se lee un archivo es buena practica cerrarlo al dejarlo de usarlos


#APPEND

#agregaremos mas lineas a nuestro archivos
c.write('\nAgregaremos una nueva linea :D')
x = open(here+'\\'+'file.txt')
#al usarlo de esta manera eliminaremos el contenido completo y solo agregaremos lo que se envie 
print(x.read())
c.close()