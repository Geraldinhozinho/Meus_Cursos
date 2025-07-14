from lib.leiaInt import leiaInt

        
def linha (tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    

def menu (lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1;34m[{c}] - \033[1;32m{item}\033[m')
        c = c +1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc

def cadastro_nome(nome):
    n = str(input(nome))
    if n.isnumeric() or n == '':
        while True:
            print('\033[1;31mERRO: por favor digite usando caracteries válidos.\033[m')
            n = str(input(nome))
            if n.isnumeric() == False and n != '':
                break
    return n