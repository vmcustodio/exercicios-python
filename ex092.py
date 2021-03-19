#faça um programa que mostre a tabuada de varios numeros, um de cada vez,para cada valor digitado pelo usuario.O programa sera interrompido quando o numero solicitado for negativp
n = 0
while True:
    n = int(input('Digite um numero inteiro para ver sua tabuada: '))
    if n < 0:
        break
    for c in range(1,11):
        print('{} X {} = {}'.format(n,c,n*c))
print('Oops... você digitou um numero negativo!')
