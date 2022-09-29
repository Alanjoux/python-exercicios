velocidade = float(input('Qual sua velocidade atual? '))
if velocidade > 80:
    print('MULTADO! Você exedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80) * 7
    print('Você foi multado em R${:.2f}!'.format(multa))
else:
        velocidade <= 80
        print('Tenha um bom dia! Dirija com segurança.') 
