from math import hypot
nun = float(input('Comprimento do cateto oposto: '))
nun1 = float(input('Comprimento do cateto adjacente '))
nun2 = hypot(nun, nun1)
print('A hipotenusa vai medir {:.2f}.'.format(nun2))


