#faça um programa que jogue par ou impar com o computador, O jogo só sera interrompido quando o jogador PERDER, mostrando o total de vitorias consecutivas que ele conquistou.
from random import randint
c = 0
while True:
    jog = int(input('Digite um numero entre 0 e 10: '))
    comp = randint(0,10)
    tot = jog+comp
    n = ' '
    while n not in 'PpIi':
        n = str(input('PAR ou IMPAR? [p/i]: ')).strip()
    print(f'Você jogou o numero {jog} e o computador jogou o numero {comp}, com o total de {tot}')
    if n in 'pP':
        if tot % 2 ==0:
            print('Você ganhou!')
            c+=1
        else:
            print('Você perdeu')
            break
    elif n in 'Ii':
        if tot%2!=0:
            print('Você ganhou')
        else:
            print('Você perdeu')
            break
print(f'Você venceu {c} vezes')