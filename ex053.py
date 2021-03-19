nome = str(input('Qual seu nome?')).lower()
if nome == 'vanessa':
    print('Que nome bonito')
elif nome== 'pedro' or nome == 'maria' or nome== 'paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'ana claudia jessica juliana':
    print('Belo nome, {}'.format(nome))
else:
    print('seu nome é normal')
print ('TENHA UM BOM DIA, {}!'.format(nome)) 