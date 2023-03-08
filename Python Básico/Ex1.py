#Recebe as notas do aluno
nota1 = float(input('Nota da primeira prova: '))
nota2 = float(input('Nota da segunda prova: '))
nota3 = float(input('Nota da terceira prova: '))

#Calcula a media
media = (nota1 + nota2 + nota3)/3

#Opção 2: solução em forma de função
def calcularMedia(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    return media

#Avalia se o aluno está aprovado ou não
if (media >= 7.0):
    print('Aprovado')
else:
    print('Reprovado')




