#elabore um programa que calcule o valor a ser pago considerando o seu preço normal e condição de pagamento:
#a vista dinheiro/cheque: 10%de desconto \\ a vista no cartao:5% de desconto \\ em ate 2x no cartao:preço normal
#3x ou mais no cartap:20% de juros
preço = float(input('Qual o preço da peça? '))
print('''FORMAS DE PAGAMENTO:
[1] a vista dinheiro/cheque
[2] a vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input(' qual a forma de pagamento? '))
if opção ==1:
    total = preço - (preço*0.1)
elif opção == 2:
    total = preço - (preço*0.05)
elif opção == 3:
    total = preço
    parcela = total/2
    print('sua compra será parcelada em 2x de R$ {}'.format(parcela))
elif opção==4:
    total = preço + (preço*0.2)
    totaparc = int(input('quantas parcelas?'))
    parcela = total / totaparc
    print('sua compra será parcelada em {}x de R$ {:.2f} com juros de 20%'.format(totaparc,parcela))
print ('sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))

