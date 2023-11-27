# While Loop
i = 0

while i < 5: 
    #print(i)
    i += 1

# While break y continue

while i < 5: 
    i += 1
    if i == 3: 
        continue
    #print(i)

#For loop [se usa sobre secuencias de datos comunmente, listas, arreglos, diccionarios]

usuarios = ['Chanchito feliz','felipe','roberto','nicolas']

"""for usuario in usuarios:
    print(usuario)

usuario2 = 'chanchito'
for c in usuario2:
    print(c)
"""
#tambien podemos usar la palabra reservada de break 

for usuario in usuarios:
    if usuario == 'roberto':
        continue
    print(usuario)

# uso de range 
# range(n) comenzara desde 0
# range(n,n) comenzara desde el primer numero dado, hasta el ultimo
# range(n,n,n) comenzara desde el primer numero dado, hasta el segundo numero dado, en saltos determinados por el tercer numero

for x in range(3,30,2):
    print(x)
else:
    print('Hemos terminado')

#For anidados

edades = [24,25,26,32]

for usuario in usuarios:
    for edad in edades:
        print(usuario, edad)


