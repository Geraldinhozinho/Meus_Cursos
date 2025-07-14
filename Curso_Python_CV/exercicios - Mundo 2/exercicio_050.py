soma = 0
for c in range(1,7):
    valor = int(input('Digite o valor {}º: '.format(c)))
    if valor % 2 == 0:
        soma += valor
        print('{}, o valor soma'.format(valor))
    else:
        print('{}, o valor não soma'.format(valor))

print('\033[1;31m{}\033[1;32m, esse é o valor da soma\033[m'.format(soma))

