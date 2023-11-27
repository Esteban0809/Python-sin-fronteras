import modulos as xs # <- como cambiar el nombre con as a los modulos
from camelcase import CamelCase

print(xs.mascotas)
xs.saludo('Ippo')

#Seleccionando lo importado
# from modulos import saludo <- esta seria la forma para poder importar unicamente el saludo sin la constante de mascotas

#Importando usando PIP, usando, listando y eliminando modulos para

# PIP es una herramienta que nos permite gestionar los modulos que tenemos instalados, ver la lista de los modulos instalados y eliminarlos

# para usarlo debemos escribir lo siguiente: pip install {nombre del modulo}
# como no es posible aprender todos los modulos disponibles podemos usar una pagina web que contenga los paquetes de python para poder buscar los modulos
# que nos interesen
# la pagina es pypi.org

#usaremos camelcase 0.2

# para poder instalarlo tendriamos que usar: pip install calmecase

c = CamelCase()
s = 'esta oracion necesita CamelCase'
print(c.hump(s))

# LISTAR MODULOS

# para listar los modulos que tenemos instalados en nuestro ordenador podemos usar el comando: pip list

# ELIMINAR UN MODULO

# para eliminar un modulo podemos usar el siguiente comando: pip uninstall camelcase
