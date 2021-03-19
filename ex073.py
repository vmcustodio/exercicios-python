#faça um programa que leia um numero inteiro e diga se ele é um numero primo ou não
n = int(input('Digite um numero: '))
div = 0
for c in range(1, n+1):
    if n%c==0:
        print(c,end=' ')
        div += 1
    else:
        print(c,end=' ')
print('\n o numero {} foi divisivel o total de: {} vezes'.format(n,div))
if div == 2:
    print('é um numero primo')
else:
    print('não é um numero primo')