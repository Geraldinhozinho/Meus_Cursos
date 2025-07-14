def leiaInt (valor):
    while True:
        try:
            n = int(input(valor))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: por favor digite um numero inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31mERRO: Entrada de dados interrompida.\033[m')
            return 0
        else:
            return n

def leiaFloat (valor):
    while True:
        try:
            n = float(input(valor))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: por favor digite um numero real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31mERRO: Entrada de dados interrompida.\033[m')
            return 0
        else:
            return n
num = leiaInt('Digite o valor inteiro: ')
num2 = leiaFloat('Digite o valor real: ')
print(f'O valor inteiro digitado foi {num} e o real foi {num2}')
