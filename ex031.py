'''distancia = float(input('Quan a distância da sua viagen? '))
if distancia <= 200:
    print('Você esta preste a começar uma viagen de {}.0Km.'.format(distancia))
    preco1 = distancia * 0.50
    print('E o preço da sua passagem será de R${:.2f}'.format(preco1))
else:
    distancia > 200
    print('Você esta preste a começar uma viagen de {:.2f}Km.'.format(distancia))
    preco2 = distancia * 0.45
    print('E o preço da sua passagem será de R${:.2f}'.format(preco2))'''


distancia = float(input('Quan a distância da sua viagen? '))
print('Você esta preste a começar uma viagen de {:.2f}Km.'.format(distancia))
if distancia <=200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))

'''distancia = float(input('Quan a distância da sua viagen? '))
print('Você esta preste a começar uma viagen de {:.2f}Km.'.format(distancia))
preco = distancia * 0.50 if <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))'''