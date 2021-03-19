#melhore o jogo do desafio 28 onde o computador vai pensar em um numero entre 0 e 10. só que agora o jogador vai tentar adivinhar ate acertar, mostrando no final quantos palpites foram necessarios para vencer
from random import randint
escolhido = randint(0,10)
palpites = 0
print('-'*20)
numero = int(input( 'Qual seu palpite para o numero que foi sorteado?'))
while numero != escolhido:
    if numero != escolhido:
      if numero < escolhido:
        print('Mais...Tente novamente')
      elif numero > escolhido:
            print('Menos...Tente novamente')
    numero = int(input('Qual seu palpite para o numero que foi sorteado?'))
    palpites += 1
print ('PROCESSANDO...')
print('-'*20)
print ('O numero sorteado foi: {}, você venceu'.format(escolhido))
print('Foram necessarios {} palpites para vencer!'.format(palpites))
