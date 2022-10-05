print('-=-' * 10)
print('Analisador de Triângulos')
print('-=-' * 10)
l1 = float(input('Primeiro Segmento: '))
l2 = float(input('Segunfo Segmento: '))
l3 = float(input('Terceiro Segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos PODEM FORMA triângulo! ')
else:
    print('Os segmentos NÃO PODEM FORMA triângulo! ')
