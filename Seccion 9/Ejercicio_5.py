# escribir una funcion que indique si el usuario es mayor de edad

def esMayor(usuario):
    return usuario.edad > 17

class Usuario:
    def __init__(self,edad):
        self.edad = edad

usuario = Usuario(15)
usuario2 = Usuario(22)

resultado1 = esMayor(usuario)
resultado2 = esMayor(usuario2)

print(resultado1)
print(resultado2)