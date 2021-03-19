#crie um programa que simule o funcionamento de um caixa eletronico. no inicio pergunte ao usuario qual sera o valor a ser sacado, e o programa vai informar quantas cedulas de cada valor serão entregues.Considerando que o caixa possui cedulas de 50,20,10 e 1
valor = int(input('Qual valor a ser sacado? R$'))
tot = valor
totced = 0
while True:
    if tot >= 50:
        tot - 50
        totced +=1
    elif tot <50:
        tot - 20
        totced +=1
    elif tot <20:
        tot - 10
        totced +=1
    elif tot ==10:
        tot - 10
        totced +=1
    else:
        tot<10
        tot -1
        totced +=1
print(f'{tot} cedulas de {} valor')



