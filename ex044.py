# Desenvolva um programa que pergunte a distancia de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200km e R$0,45 para viagens mais longes
viagem = float(input('Qual a distancia da viagem em km?'))
if viagem <= 200:
    preco = (0.50*viagem)
    print('o preço da passagem será de R${}'.format(preco))
else:
    preco2 = (0.45*viagem)
    print('o preço da passagem será de R${:.2f}'.format(preco2))
#preço = viagem * 0.5 if viagem <= 200 else viagem*0.45