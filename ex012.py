preco = float(input('Digite o preço do produto R$'))
novo = preco - (preco * 5/100)
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, novo))

