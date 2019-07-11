def divisores (num):
    return [x for x in range (1,num) if num % x==0]

def divisores_rec (num,aux):
    if aux == num:
        return []
    if num % aux ==0:
        return [aux] + divisores_rec (num, aux+1)
    return divisores_rec (num, aux+1)


def perfecto (numero):
    return sum(divisores(numero))== numero
perf=0
lista2=[]
while len(lista2)<4:
    perf+=1
    if perfecto (perf):
        lista2.append(perf)
print lista2
