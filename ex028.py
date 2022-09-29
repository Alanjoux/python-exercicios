from random import randint
computador = randint(0, 5) # Faz o computador sortear um número
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' *20)
jogador = int(input('Em que numero eu pensei? '))
if jogador == computador:
    print('Você acertou parabéns.')
else:
    print('Você errou tente outra vez.')
print('O número escolhido pelo computador foi {}'. format(computador))        