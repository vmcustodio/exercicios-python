#crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços
frase = str(input('Digite uma frase: ')).replace(' ','')
b = True
c = len(frase)
for x in range(c):
    if frase[x] != frase[c-1-x]:
        b= False
        break
if b:
    print(' é um palindromo')
else:
    print('não é um palindromo')

