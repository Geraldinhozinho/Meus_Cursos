a1 = int(input('digite o primeiro termo: '.capitalize()))
r = int(input('digite a razão: '.capitalize()))
quantidade = 0
contador = 0
mais = 5
while mais != 0:
    quantidade = quantidade + mais
    while contador < quantidade:
        print(a1,end=' - ')
        a1 = a1 + r
        contador += 1
    print('PAUSA')
    mais = int(input('deseja mostrar mais termos? Mais quantos: '.upper()))
                
print('Acabou {} termos mostrados'.format(contador))

        
# a1 = int(input('digite o primeiro termo: '.capitalize()))
# r = int(input('digite a razão: '.capitalize()))
# quantidade = 5
# contador = 0
# mais = ''
# while mais != 0:
#     while contador < quantidade:
#         print(a1,end=' - ')
#         a1 = a1 + r
#         contador += 1
        
        
#         if contador == quantidade:
#             mais = int(input('deseja mostrar mais termos? Mais quantos: '.upper()))
#             if mais > 0:
#                 quantidade = quantidade + mais
#                 print(a1,end=' - ')
#                 a1 = a1 + r
#                 contador += 1
                
# print('Acabou {} termos mostrados'.format(contador))
