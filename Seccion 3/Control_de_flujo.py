#Instruccion IF
if 2 < 5:
    print("2 no es mayor")
else:
    print("2 es mayor")

#comparaciones simples que podemos hacers
# a == b
# a < b
# a > b
# a != b
# a <= b 
# a >= b

#if 2 == 2:
#    print("2 es igual a 2")

#if 2 == 3:
#    print("2 es igual a 3")

#if 2 > 5:
#    print("2 es mayor a 5")

#if 5 > 2:
#    print("5 es mayor a 2")

#if 2 != 2:
#    print("2 es distinto a 2")

#if 3 != 2:
#    print("3 es distinto a 2")

#if 3 <= 2:
#    print("3 es menor o igual a 2")

#if 3 >= 2:
#    print("3 es mayor o igual a 3")

# IF, ELIF  y else

if 2 > 5:
    print("2 es menor a 5 en if")
elif 2 == 5: # ejecutara si el if es verdadera y se puede encadenar todas las veces que queramos
    print("2 menor a 5 en el elif")
elif 2 < 5: 
    print("2 menor a 5 en el segundo elif")
else: # se ejecutara si todas las anteriores ejecutan en falso
    print("2 es igual a 2")

if 2 > 5:
    print("dos es menor a 5 en if")
else:
    print("yo me imprimo solo si todo lo anterior se valua en falso")


#IF cortos y TERNARIOS

#if corto
if 2 < 5: print('if de una sola linea') 

#if ternario
print('cuando vuelve true') if 5 < 2 else print('cuando devuelve false')

#Uso de AND
if 2 < 5 and  3 > 2: print('ambas devuelven true')

if 2 < 5 and  3 > 5: print('una falsa, no se mostrara')

#Uso de OR
if 2 > 3 or 1 == 1:
    print("True, se imprime con que una se cumpla")










