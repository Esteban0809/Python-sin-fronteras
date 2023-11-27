# escribir una funcion que encuentre el elemento menor de una lista

lista = [1,2,3,4,5,66,77,-111]

def menor_de_lista(lista):
    menor = 'init'
    for x in lista:
        if menor == 'init':
            menor = x
        else:
            menor = x if  x < menor else menor
    print('menor',menor)

menor_de_lista(lista)