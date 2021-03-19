#crie um programa que leia varios numeros inteiros pelo teclado, só para quando o usuario digitar o valor 999. no final, mostre quantos numeros foram digitados e qual foi a soma entre eles, desconsiderando o flag
n = 0
s = 0
c = 0
while True:
    n = int(input('Digite um numero  ou digite 999 para parar: '))
    if n == 999:
        break
    s += n
    c+=1
print(f'Você digitou {c} numeros com a soma de {s}')