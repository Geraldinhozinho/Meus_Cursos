def Opcao(msg):
    import time
    while True:
        try:
            print('-'*30)
            print('menu principal'.upper().center(30))
            print('-'*30)
            print('[1] - Ver pessoas cadastradas')
            print('[2] - Cadastrar nova pessoa')
            print('[3] - Sair do sistema')
            escolha = int(input('Sua opção: ').strip())
            if escolha == 1:
                print('-'*30)
                print('Opção 1'.upper().center(30))
                print('-'*30)
            elif escolha == 2:
                print('-'*30)
                print('Opção 2'.upper().center(30))
                print('-'*30)
            elif escolha == 3:
                print('-'*30)
                print('Opção 3'.upper().center(30))
                print('-'*30)
                print('Saindo do sistema...') 
                time.sleep(1)
                print('Até logo!')
                break
                # print('\033[1;31mERRO! Por favor, digite um número inteiro válido\033[m')
            elif escolha > 3 or escolha < 1:
                print('\033[1;31mERRO! digite uma opção válida\033[m')
        except (ValueError):
            print('\033[1;31mERRO! Por favor, digite um número inteiro válido\033[m')
        except (KeyboardInterrupt):
            print('\033[1;31mERRO! Por favor, digite alguma opção\033[m')
msg = 'ola'
Opcao(msg)