#faça um prgrama que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 ate 0, com uma pausa de 1 segundo entre elas.
from time import sleep
for c in range(10,-1, -1):
    print(c)
    sleep(1)
print('Que comecem os fogos de artificio!')
