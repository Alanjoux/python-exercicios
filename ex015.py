dia = float(input('Quantos dias o carro ficou alugado? '))
v1 = dia * 60
km = float(input('Quantos km o carro rodou? '))
v2 = km * 0.15
total = v1 + v2
print('O total a pagar é de R${:.2f}'.format(total))
