print('-----TABUADA-----')
valor = int(input('Digite um valor: '))
for n in range(0, 11):
    print(valor, '*' , n, '=', '{:^10}'.format(valor * n))
    