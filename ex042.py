#'Escreva um programa que leia a velocidade de um carro'
#'Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado'
#('A multa vai custar R$7,00 por cada Km acima do limite.')
vel = float(input(' escreva a velocidade do carro:'))
if vel > 80:
    print ('Você ultrapassou a velocidade permitida, e será multado!')
    multa = (vel - 80)*7
    print ('o valor da multa será de R${:.2f}'.format(multa))
else:
    print('Você não ultrapassou a velocidade permitida')
