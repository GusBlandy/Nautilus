lista1 = list(input('Insira as notas da Prova 1 (Ex: 7.0 2.0 4.0 5.0 ...): ').split()) 
lista2 = list(input('Insira as notas da Prova 2: ').split())
lista3 = list(input('Insira as notas da Prova 3: ').split())

print()

#Função para calcular a média
def calcularMedia(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    return media

#Checar se o aluno foi aprovado ou não
for i in range(10):
    if (calcularMedia(float(lista1[i]), float(lista2[i]), float(lista3[i])) >= 7.0):
        print(f'Aluno{i+1}: Aprovado')
    else:
        print(f'Aluno{i+1}: Reprovado')