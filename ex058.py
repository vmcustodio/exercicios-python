#crie um programa que leia duas notas de um aluno e calcule sua media, mostrando no final:
#media abaixo de 5.0:reprovado, media entre 5.0 e 6.9: recuperação, media 7.0 ou superior: aprovado
n1 = float(input('Escreva a nota da primeira prova: '))
n2 = float(input('Escreva a nota da segunda prova: '))
media = (n1+n2)/2
if media < 5:
    print('REPROVADO')
elif 5 < media < 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')