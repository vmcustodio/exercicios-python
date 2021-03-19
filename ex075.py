#crie um programa que leia o ano de nascimento de sete pessoas. no final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores.
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1,8):
    nasc = int(input('Digite a data de nascimento: '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('O total de pessoas maiores de idade é de: {} e menores de idade é de: {}'.format(totmaior,totmenor))