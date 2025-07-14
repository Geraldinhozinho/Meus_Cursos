def fatorial(numero, show = False):
    if show == True:
        for cont in range(numero, 0, -1):
            if cont == numero:
                print(f'{cont}!',end=' x ')
            elif cont > 1:
                print(cont, end=' x ')
            else:
                print(cont, end=' = ')
            fatorial = 1
        for cont in range(1, numero + 1):
            fatorial = fatorial * cont
        print(f'{fatorial}')
    if show == False:
        fatorial = 1
        for cont in range(1, numero + 1):
            fatorial = fatorial * cont
        print(f'O fatorial de {numero}! é {fatorial}')

v = int(input('Digite um valor: '))
c = ''
while c not in ('s', 'n'):
    c = str(input('Deseja ver o calculo [s / n]: ')).lower().strip()[0]
    if c == 's':
        show = True
    if c != 's' and c != 'n':
        print('ops! tente novamente... apenas [s ou n]')
    if c == 'n':
        show = False
        break
print('-' * 20)
fatorial(v, show)
print('-' * 20)
help(fatorial)