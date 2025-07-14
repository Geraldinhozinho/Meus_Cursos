V1 = int(input('\033[1;32mDigite um valor: '))
V2 = int(input('Digite um segundo valor: '))
V3 = int(input('Digite um terceiro valor: '))
print('\033[m')
if V1 > V2 and V1 > V3:
    print('O maior valor é: {}'.format(V1))
if V2 > V1 and V2 > V3:
    print('O maior valor é: {}'.format(V2))
if V3 > V1 and V3 > V2:
    print('O maior valor é: {}'.format(V3))
if V1 < V2 and V1 < V3:
    print('O menor valor é: {}'.format(V1))
if V2 < V1 and V2 < V3:
    print('O menor valor é: {}'.format(V2))
if V3 < V1 and V3 < V2:
    print('O menor valor é: {}'.format(V3))
