#Escreva um programa que faça o computador pensar um numero de 0 a 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador
#O programa deverá escrever na tela se o usuário venceu ou perdeu
import random
from time import sleep
escolhido = random.randint(0,5)
print('-'*20)
numero = int(input( 'Qual numero você acha que foi sorteado?'))
print ('PROCESSANDO...')
sleep(4)
print('-'*20)
print ('o numero sorteado foi:', escolhido)
if numero == escolhido:
    print('você venceu!')
else:
    print('voce perdeu')