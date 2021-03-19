#refaça o desafio da PA, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
n1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
dec = n1 + (10-1) * razao
while n1<=dec:
    print(n1,end=' ')
    n1 += razao
