matriz = []
matriz.append(range (1,4))
matriz.append(range (4,7))
print matriz
for i in matriz:
    for j in i:
        print j
matriz.append([10,11,51])
print matriz

i="123"
digitos=[int(x)for x in list(i)]
print digitos
