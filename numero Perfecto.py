def divisores (num):
    return [x for x in range (1,num) if num % x==0]

def divisores_rec (num,aux):
    if aux == num:
        return []
    if num % aux ==0:
        return [aux] + divisores_rec (num, aux+1)
    return divisores_rec (num, aux+1)

def Lista_n_p (lista):
    lista =
    lista.append(
    if len(

def perfecto (numero):
    return sum(divisores(numero))== numero

n
def suma (lista1):
    m = 0
    for i in lista1:
        m+=i
    return m

n = input  (" ingrese el numero")
listadiv = divisores_rec (n,1)
if suma (listadiv)==n:
    print "numero perfecto"



#if sum (listadiv)== n:
 #   print "numero perfecto"
#else:
 #   print "numero imperfecto"

print listadiv
