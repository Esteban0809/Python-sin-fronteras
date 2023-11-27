# escribir una funcion que reciba nombre y apellido y los vaya agregando a un archivo

def agregarNombreAArchivo(nombre, apellido):

    c = open('nombrecomleto.txt', 'a')
    c.write(nombre + ' ' + apellido + '\n')
    c.close()

agregarNombreAArchivo('Josue', 'Torres')