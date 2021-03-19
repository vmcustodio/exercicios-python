#desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem ou não formar um triangulo
r1 = float(input('digite o comprimento da primeira reta: '))
r2 = float(input('digite o comprimento da segunda reta: '))
r3 = float(input('digite o comprimento da terceira reta: '))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('as retas acima podem formar um triangulo')
else:
    print('as retas acima não podem formar um triangulo')