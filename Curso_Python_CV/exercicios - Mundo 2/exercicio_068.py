import random
contador = 0




while True:
    computador = random.randint(0,10)
    print(computador)
    print(10*'-',' PAR OU ÍMPAR ',10*'-')
    escolha = str(input('Escolha PAR / ÍMPAR: '.upper()).upper())
    numero = int(input('digite o número: '.upper()).upper())   
   
   
    if numero > 10 and escolha != 'P' and escolha != 'I':
        print('Opção inválida - Apenas números menores ou igual a 10')
        print('Opção inválida - Apenas P ou I')
        print('Vamos tentar denovo...')
    elif numero > 10:
        print('Opção inválida - Apenas números menores ou igual a 10')
        print('Vamos tentar denovo...')
        
    elif escolha != 'P' and escolha != 'I':
        print('Opção inválida - Apenas P ou I')
        print('Vamos tentar denovo...')
    
    else:   
        resultado = computador + numero
        if escolha == 'P':
            if resultado % 2 == 0:
                print('\nJOGADOR VENCEU')
                print(20*'-')
                print(f'{numero} + {computador} = {resultado} / PAR')
                print(20*'-')
                print('VAMOS JOGAR NOVAMENTE...\n')
                contador = contador + 1
            else:
                print('\nCOMPUTADOR VENCEU')
                break
        elif escolha == 'I':
            if resultado % 2 == 1:
                print('\nJOGADOR VENCEU\n')
                print(20*'-')
                print(f'{numero} + {computador} = {resultado} / ÌMPAR')
                print(20*'-')
                print('VAMOS JOGAR NOVAMENTE...\n')
                contador = contador + 1
            else:
                print('\nCOMPUTADOR VENCEU\n')
                break
        else:
            print('')
            # print('Opção inválida - Apenas P ou I')
            # print('Opção inválida - Apenas números menores ou igual a 10')
            # print('Vamos tentar denovo...')
        
print(f'ACABOU... VOCÊ GANHOU {contador} vezes')