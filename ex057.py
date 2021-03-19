#faça um programa que leia o ano de nascimento de um jovem e informe,de acordo com sua idade
#se ele ainda vai se alistar no serviço miliar, se é a hora de se alistar, se já passou do tempo de alistamento, também deverá mostrar o tempo que falta ou passou do prazo
ano = int(input('Qual o ano do seu nascimento? '))
anoat = int(input('Qual ano atual?'))
idade = int(anoat-ano)
if idade == 18:
    print('Você está na idade de se alistar!')
elif idade < 18:
    print ('Você ainda não está na idade de se alistar, faltam {} anos'.format(18-idade))
else:
    print('Você passou do prazo para se alistar, se passou {} anos'.format(idade-18))