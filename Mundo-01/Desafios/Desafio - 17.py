from math import hypot
numero1 = float(input('Comprimento do cateto oposto: '))
numero2 = float(input('Comprimento do cateto adjacente: '))
resultado = hypot(numero1,numero2)
print('A hipotenusa vai medir {:.2f}'.format(resultado))