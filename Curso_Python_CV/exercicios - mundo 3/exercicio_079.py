


lista = []
while True:
    v1 = int(input('digite um valor: '.capitalize()))
    if v1 not in lista:
        lista.append(v1)
    else:
        print('já existe na lista'.upper())
        
    continua = str(input('Continua [S / N]: ').upper())[0]
    if continua == 'N':
        break
    # Caso a resposta não seja 'N', verifica se é 'S', senão pede novamente
    while continua != 'S' and continua != 'N':
        print('Opção inválida. Por favor, digite apenas S ou N.')
        continua = str(input('Continua [S / N]: ').upper())[0]
print('Os valores digitados foram: ', end=' ') 
lista.sort()   
for valor in lista:
    print(f'{valor}', end=' ')