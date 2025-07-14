# lista = []
# contp = conti = 0
# while True:
#     valor = int(input('Digite um valor: '))
#     lista.append(valor)
#     continua = ''
#     while continua not in ('S', 'N'):
#         continua = input('Deseja continuar? [S / N]: ').strip().upper()[0]
#         if continua != 'S' and continua != 'N':
#             print('tente novamente... '.upper(),end='')
#     if continua == 'N':
#         break
# print(f'Todos os valores digitados foram: {lista}')
# print(f'Todos os valores pares digitados foram: ',end='')
# for cont, valores in enumerate(lista):
#     if lista[cont] % 2 == 0:
#         print(valores,end= ' ')
#         contp = contp +1
# if contp ==0:
#     print('Não há valores digitados',end='')    
# print(f'\nTodos os valores ímpares digitados foram: ',end='')
# for cont, valores in enumerate(lista):
#     if lista[cont] % 2 == 1:
#         print(valores,end= ' ') 
#         conti = conti +1   
# if conti ==0:
#     print('Não há valores digitados')    


lista = []
listapar = []
listaimpar = []

contp = conti = 0
while True:
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0 :
        listapar.append(valor)
        contp = contp +1
    else:
        if valor % 2 == 1 :
            listaimpar.append(valor)
            conti = conti +1
    lista.append(valor)
    continua = ''
    while continua not in ('S', 'N'):
        
        continua = input('Deseja continuar? [S / N]: ').strip().upper()[0]
        if continua != 'S' and continua != 'N':
            print('tente novamente... '.upper(),end='')
            
    if continua == 'N':
        break
    

print(f'Todos os valores digitados foram: {lista}')
if contp > 0:
    print(f'Todos os valores pares digitados foram: {listapar}') 
else:
    print('Não há valores digitados pares digitados')    
if conti > 0:  
    print(f'\nTodos os valores ímpares digitados foram: {listaimpar}')
else:
    print('Não há valores digitados ímpares digitados') 
   