#melhore o desafio anterior da PA, perguntando para o usuario se ele quer mostrar mais alguns termos. o programa encerra quando ele disser que quer mostrar 0 termos
n1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
dec = n1 + (10-1) * razao
while n1<=dec:
    print(n1,end=' ')
    n1 += razao







