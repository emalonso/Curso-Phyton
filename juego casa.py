from random import randint # llamar a la funcion randin de la libreria random
lista = []
for i in range (100): # le doy un rango de 100 veces hacer la prueba
    n1 = randint(0,9) # solo permite darles valores a n1 de valores del 0 a 9
    if not n1 in lista:  # compara que si no esta en la lista lo agrege a la lista
        lista.append(n1) # incluya el numero en la lista        
    if len(lista) == 3:  #le pone un maximo a la lista de 3
        break # rompe el cliclo
print lista # imprime la lista

#for i in range (5):

a= raw_input ("ingrese su valor de tres dijitos: ") #ingresa el valor
if not len (a) == 3:
    print "no has ingresado 3 digitos, intenta nuevamente"
    
digitos=[int(x)for x in list(a)] # convierte la lista en numeros enteros
print digitos


""" comparacion de """
def comparar_FP(lista):
    var1=0
    contadorf = 0
    contadorp = 0
    for i in range (len (digitos)):
        if lista[var1]==digitos[i]:
            contadorf+=1
        elif digitos[i] in lista:
            contadorp+=1
        var1+=1
    return contadorf,contadorp

fijas,picas = comparar_FP (lista)
print "usted a ingresado " + str(fijas) + " fijas " + "usted a ingresado " + str(picas)+ " picas"


            
