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

