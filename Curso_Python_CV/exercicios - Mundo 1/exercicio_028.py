import random
import time
lista = [0, 1, 2, 3, 4, 5]

numero = random.choice(lista)
numero_user = int(input('Escolha um número de 0 a 5: '))
print('PROCESSANDO...')
time.sleep(2)
if numero == numero_user:
    print('O número escolhido pelo computador foi {}'.format(numero))
    print('Parabéns você acertou, seu número foi {}'.format(numero_user))
else:
    print('O número escolhido pelo computador foi {}'.format(numero))
    print('Poxa, que pena, você errou, seu número foi {}'.format(numero_user))