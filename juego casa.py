from random import randint # llamar a la funcion randin de la libreria random
lista = []
for i in range (100): # le doy un rango de 100 veces hacer la prueba
    n1 = randint(0,9) # solo permite darles valores a n1 de valores del 0 a 9
    if not n1 in lista:  # compara que si no esta en la lista lo agrege a la lista
        lista.append(n1) # incluya el numero en la lista        
    if len(lista) == 3:  #le pone un maximo a la lista de 3
        break # rompe el cliclo
print lista # imprime la lista

for i in range (5):
    a= input ("ingrese su valor de tres dijitos: ") #ingresa el valor
