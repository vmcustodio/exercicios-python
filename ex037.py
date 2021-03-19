frase= str(input('digite uma frase: ')).strip().upper()
print(' A quantidade de letras A existente na frase é de:' , frase.count('A'))
print('a primeira letra A apareceu na posição', frase.find('A')+1)
print('a ultima letra A apareceu na posição: ', frase.rfind('A')+1)