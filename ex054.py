#escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
#o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar
#calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o emprestimo sera negado
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o valor do seu salario? R$'))
ano = int(input('Em quantos anos você deseja pagar? '))
prestacao = casa/(ano*12)
minimo = salario*0.3
print('Para pagar a casa no valor de R$ {:.2f} em {} anos, a prestação mensal será de {:.2f}'.format(casa, ano,prestacao))
if prestacao <= minimo:
    print('Emprestimo APROVADO')
else:
    print('Emprestimo NEGADO')