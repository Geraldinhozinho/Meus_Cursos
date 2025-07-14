lista = []

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    
    continua = ''
    while continua not in ('S', 'N'):
        continua = input('Deseja continuar? [S / N]: ').strip().upper()[0]
        if continua != 'S' and continua != 'N':
            print('tente novamente... '.upper(),end='')
            
    if continua == 'N':
        break
    
print(f'Você digitou {len(lista)} elementos ')
lista.sort(reverse= True)

print(f'Os valores em ordem decrescente são {lista}')
if 5 not in lista:
    print('O valor 5 não está na lista')
else:
    print('O valor 5 está na lista')