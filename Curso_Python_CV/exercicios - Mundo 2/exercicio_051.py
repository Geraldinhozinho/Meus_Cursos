
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
decimo = a1 + (11 - 1) * r
cont = 0
for i in range(a1,decimo,r):  # Para exibir os 10 primeiros termos
    cont += 1
    print('{}º Termo = {} - '.format(cont, i), end='')  
print('Acabou')

    
    

    