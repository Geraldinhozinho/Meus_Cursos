import time
def contador(i, f, p):
    print(30*'-')
    print(f'Contagem de {i} até {f} de {p} em {p}')
    time.sleep(2)
    if p < 0:
        p = p * -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}',end=' ', flush=True)
            cont = cont + p
            time.sleep(0.5)
    else:
        cont = i
        while cont >= f:
            print(f'{cont}',end=' ', flush=True)
            cont = cont - p
            time.sleep(0.5)
    print('\n',30*'-')
    

contador(1,10,1)
contador(10,0,2)
print('\n',30*'-')
print('Hora de personalizar')
print('\n',30*'-')
contador(
    
    
    i = int(input('Valor de ínicio: ')),
    f = int(input('Valor de finalização: ')),
    p = int(input('Passos: '))

)