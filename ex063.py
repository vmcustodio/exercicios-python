#crie um programa que faça o computador jogar jokenpo com voce
from random import randint
itens = ('pedra', 'papel','tesoura')
computador = randint(0,2)
print('''ESCOLHA SUA JOGADA
[0] pedra
[1] papel
[2] tesoura''')
jogador = int(input('qual é sua jogada?'))
print('-='*11)
print('computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if computador ==0:
    if jogador ==0:
        print('empate')
    elif jogador ==1:
        print('jogador venceu')
    elif jogador ==2:
        print('computador venceu')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:
    if jogador == 0:
        print('computador venceu')
    elif jogador == 1:
        print('empate')
    elif jogador == 2:
        print('jogador venceu')
    else:
        print('JOGADA INVALIDA')
elif computador ==2:
    if jogador == 0:
        print('jogador venceu')
    elif jogador == 1:
        print('computador venceu')
    elif jogador == 2:
        print('empate')
    else:
        print('JOGADA INVALIDA')
