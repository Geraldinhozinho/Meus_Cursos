numero = int(input('Digite um numero: '))
cont = 0
for c in range(1,numero +1):
    if numero == 1:
        cont = 1
    elif numero % c == 0:
        print('\033[1;32m{}'.format(c), end=' ')
        cont += 1
    else:
        print('\033[1;31m{}'.format(c), end=' ')

if cont == 1:
    print('\n\033[mO número {} é primo '.format(numero))
elif cont > 2:
    print('\n\033[mO número {} não é primo por se divide {}x'.format(numero, cont))
else:
    print('\n\033[mO número {} é primo pois se divide {}x apenas'.format(numero, cont))
        