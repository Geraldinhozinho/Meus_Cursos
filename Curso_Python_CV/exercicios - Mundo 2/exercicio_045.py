import random, termcolor, time

Lista = ['PEDRA', 'PAPEL', 'TESOURA']
Computador = random.choice(Lista)
Nome = input('\033[1;37mDIGITE SEU NOME PARA JOGAR: ')
print(10*'-~',termcolor.colored(' Vamos Jogar JOKENPÔ ','blue'),10*'-~')
print(12*'==',termcolor.colored(' CARREGANDO... ','blue'),12*'==')
print(' ')
time.sleep(2)
print(14*' ','\033[1;33m-----> SELECIONE UMA OPÇÃO  <-----\033[m')
print(12*' ','\033[1m[ 1 ] PEDRA   ', end=' ')
print('[ 2 ] PAPEL   ', end=' ')
print('[ 3 ] TESOURA')
Opcao = int(input('\033[1;33mDIGITE: '))

print('\033[1;34m-~--~--~--~--~--~--~-~ CARREGANDO... -~--~--~--~--~--~--~-~') 
time.sleep(2)  
print('\033[1;34m-~--~--~--~--~--~--~-~--~-~ JO --~-~~--~--~--~--~--~--~-~-~') 
time.sleep(0.5)  
print('\033[1;34m-~--~--~--~--~--~--~-~--~-~ KEN --~-~-~--~--~--~--~--~--~-~') 
time.sleep(0.5)  
print('\033[1;34m-~--~--~--~--~--~--~-~--~-~ PÔ --~-~-~--~--~--~--~--~--~-~-') 
time.sleep(0.5)  
print('\033[m')

if Computador == 'PEDRA' and Opcao == 3:
    print('{:^90}'.format('\033[1;37m{}\033[1;33m jogou TESOURA \033[1;31mx \033[1;37mComputador\033[1;33m jogou {}'.format(Nome, Computador)))
    print('{:^65}'.format('\033[1;31mO computador venceu!\033[m'))
    
elif Computador == 'PAPEL' and Opcao == 3:
    print('{:^90}'.format('\033[1;37m{}\033[1;33m jogou TESOURA \033[1;31mx \033[1;37mComputador\033[1;33m jogou {}'.format(Nome, Computador)))
    print('{:^65}'.format('\033[1;32m{}, você venceu!\033[m'.format(Nome)))
    
elif Computador == 'TESOURA' and Opcao == 3:
    print('{:^90}'.format('\033[1;37m{}\033[1;33m jogou TESOURA \033[1;31mx \033[1;37mComputador\033[1;33m jogou {}'.format(Nome, Computador)))
    print('{:^65}'.format('--- EMPATE ---\033[m'))

elif Computador == 'PEDRA' and Opcao == 2:
    print('{:^90}'.format('\033[1;37m{}\033[1;33m jogou PAPEL \033[1;31mx \033[1;37mComputador\033[1;33m jogou {}'.format(Nome, Computador)))
    print('{:^65}'.format('\033[1;32m{}, você venceu!\033[m'.format(Nome)))

elif Computador == 'PAPEL' and Opcao == 2:
    print('{:^90}'.format('\033[1;37m{}\033[1;33m jogou PAPEL \033[1;31mx \033[1;37mComputador\033[1;33m jogou {}'.format(Nome, Computador)))
    print('{:^65}'.format('--- EMPATE ---\033[m'))
    
elif Computador == 'TESOURA' and Opcao == 2:
    print('{:^90}'.format('\033[1;37m{}\033[1;33m jogou TESOURA \033[1;31mx \033[1;37mComputador\033[1;33m jogou {}'.format(Nome, Computador)))
    print('{:^65}'.format('\033[1;31mO computador venceu!\033[m'))

elif Computador == 'PEDRA' and Opcao == 1:
    print('{:^90}'.format('\033[1;37m{}\033[1;33m jogou PEDRA \033[1;31mx \033[1;37mComputador\033[1;33m jogou {}'.format(Nome, Computador)))
    print('{:^65}'.format('--- EMPATE ---\033[m'))

elif Computador == 'PAPEL' and Opcao == 1:
    print('{:^90}'.format('\033[1;37m{}\033[1;33m jogou PEDRA \033[1;31mx \033[1;37mComputador\033[1;33m jogou {}'.format(Nome, Computador)))
    print('{:^65}'.format('\033[1;31mO computador venceu!\033[m'))
    
elif Computador == 'TESOURA' and Opcao == 1:
    print('{:^90}'.format('\033[1;37m{}\033[1;33m jogou TESOURA \033[1;31mx \033[1;37mComputador\033[1;33m jogou {}'.format(Nome, Computador)))
    print('{:^65}'.format('\033[1;32m{}, você venceu!\033[m'.format(Nome)))
    
else:
    print('\033[1;31mOPÇÃO INVALIDA\033[m')