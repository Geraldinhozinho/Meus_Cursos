
soma = 0
cont = 0
for x in range(0,501, 3):
    if x%2 ==0:
        print('{} Par, não soma'.format(x))
    else:
        print('{} ímpar, soma'.format(x))
        soma += x
        cont += 1
print(10*'+')
print('a soma dos {} itens foi {}'.format(cont,soma))
print('FIM')