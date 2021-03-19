#mostre a tabuada de um numero que o usuario escolher
c = int(input('Digite um numero para saber sua tabuada: '))
for a in range (1,11):
    print('{} X {} = {}'.format(c,a,c*a))