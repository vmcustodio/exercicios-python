from math import radians,sin,cos,tan
angulo = float(input('Digite um ângulo qualquer: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tang = tan(radians(angulo))
print("os valores de seno, cosseno e tangente são, respectivamente: {:.2f}, {:.2f}, {:.2f}".format(sen, cos, tang))
