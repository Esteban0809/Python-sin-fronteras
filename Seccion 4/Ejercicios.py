#Ingresar datos a python
#dato = input('Ingrese dato: ')
#lista = ['hola','mundo','chanchito','feliz','dragones']

#if lista.count(dato) > 0:
    #print('El dato existe:', dato)
#else:
    #print('El dato no existe :(',dato)
#print(dato)

#Mini calculadora

primero = input('Ingrese primer numero: ')

try:
    primerNum = int(primero)
except:
    primerNum = 'Chanchito feliz'

if primerNum == 'Chanchito feliz':
    print('El valor ingresado no es un numero entero')
    exit()

segundo = input('ingrese segundo numero:')
try:
    segundoNum = int(segundo)
except:
    segundoNum = 'Chanchito feliz'

if segundoNum == 'Chanchito feliz':
    print('El valor ingresado no es un numero entero')
    exit()


simbolo = input('Ingrese operacion a realizar: ')

if simbolo == '+':
    print(primerNum + segundoNum)
elif simbolo == '-':
    print(primerNum - segundoNum)
elif simbolo == '*':
    print(primerNum * segundoNum)
elif simbolo == '/':
    print(primerNum / segundoNum)
else:
    print("El simbolo ingresado no es valido")
