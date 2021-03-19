#faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'm' ou 'f'. caso esteja errado, peça a digitação novamente até ter um valor correto'
s = str(input('Digite seu sexo [F/M]: ')).upper().strip()
while s != 'M' and s != 'F':
    print('Você digitou um sexo que não existe')
    s = str(input('Digite seu sexo [F/M]: ')).upper()
print('Obrigada!')
