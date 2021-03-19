#faça um programa que leia o nome e o preço de varios produtos. devera perguntar se o usuario vai continuar.no final mostre:
#qual é o total gasto na compra, quantos produtos custam mais de 1000, qual o nome do produto mais barato
tot = 0
totmaior = 0
menor = 0
c = 0
menor2 = ' '
while True:
    nome = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto: R$'))
    c += 1
    tot += preço
    if preço > 1000:
        totmaior += 1
    if c == 1:
        menor = preço
        menor2 = nome
    else:
        if preço < menor:
            menor = preço
            menor2 = nome
    resp = ' '
    resp = str(input('Deseja continuar? [s/n]')).strip().upper()
    if resp == 'N':
        break
print('CALCULANDO....')
print(f'O total da compra foi de : R$ {tot}, com o total de {totmaior} produtos com um preço acima de R$1000.00')
print(f'O produto mais barato foi {menor2} custando apenas R${menor}')
