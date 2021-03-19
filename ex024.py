import math
ca = float(input('Coloque o comprimento do cateto adjacente: '))
co = float(input('coloque o comprimento do cateto oposto' ))
hip = math.hypot(ca,co)
print('o comprimento da hipotenusa é de: {:.2f}'.format(hip))