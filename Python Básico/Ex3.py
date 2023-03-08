#Crindo lista usando list comprehension
listaNumeros = [numero for numero in range(1000)]

listaPar = []
listaImpar = []

#Itera sobre cada número e checa se é divisível por 2
for i in listaNumeros:
    if (i % 2 == 0):
        listaPar.append(i)
    else:
        listaImpar.append(i)

print(listaPar)
print(listaImpar)