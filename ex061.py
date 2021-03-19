#desenvolva uma logica que leia o peso e a altura de um apessoa, calcule seu IMC e mostre seu status:
#abaixo de 18.5:abaixo do peso\\entre 18.5 e 25:peso ideal\\ 25 ate 30:sobrepeso\30 ate 40:obesidade\\ acima de 40:obesidade morbida
altura = float(input('Qual sua altura? '))
peso = float(input('Qual seu peso? '))
imc = peso/(altura*altura)
print('seu IMC é de {:.2f}, e é classificado em:'.format(imc))
if imc < 10:
    print('ABAIXO DO PESO')
elif 18.5 <= imc <= 25:
    print('PESO IDEAL')
elif 25.1 <= imc <= 30:
    print('SOBREPESO')
elif 30.1 <= imc <= 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA')