listaPrimos = []

#Percorre os numeros de 1 a 1000.
for numero in range(1, 1000+1):
    listaDivisores = []
    
    #Em cada numero percorrido, checa se ele possui divisores e adicionas em uma lista.
    for i in range(1, numero+1):
        if (numero % i == 0):
            listaDivisores.append(i)

    #Checa o numero de divisores, se for 2 (dividido por 1 e por ele mesmo), é primo.    
    if (len(listaDivisores)) == 2:
        listaPrimos.append(numero)
            
print(sum(listaPrimos))