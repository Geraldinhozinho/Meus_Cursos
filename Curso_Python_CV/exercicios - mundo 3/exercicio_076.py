lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 
         'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 
         'Canetas', 22.30,  'Livro', 34.90 )
conta = 0
conto = 0
print(20*'\033[1m--')
print(10*' ','listagem de preços'.upper())
print(20*'--')
for cont in lista:
    if conto < 1:
        print(f'{lista[conta]:.<30}R$',end='')
        conto = conto +1     
    elif conto < 2:
        print(f'{lista[conta]:>8.2f}')
        conto = 0
    conta = conta +1    
print('\033[m')
