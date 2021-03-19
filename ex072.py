#desenvolva um programa que leia o primeiro termo e a razão de uma PA. no final, mostre os 10 primeiros termos dessa progressão
n1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razãp da PA: '))
dec = n1 + (10-1) * razao
for c in range(n1,dec+razao,razao):
    print('{}'.format(c), end=' ')