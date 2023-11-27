
# Multiplicar 2 numeros sin usar el simbolo de multiplicacion
a = 5
b = 100

def multiplicar(a,b):
    resultado=0
    cont = 0
    for i in range(b):
        resultado += a
    print(resultado)

multiplicar(a,b)